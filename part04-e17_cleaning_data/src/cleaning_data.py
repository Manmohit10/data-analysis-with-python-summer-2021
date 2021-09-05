#!/usr/bin/env python3

import pandas as pd
import numpy as np

def clean_names(df):
    temp=df.str.split(",| ",expand=True)
    temp[0]=temp[0].str.capitalize()
    temp[1]=temp[1].str.capitalize()
    temp[2]=temp[2].str.capitalize()
    df.loc[~df.str.contains(",")]=temp.loc[:,0]+' '+temp.loc[:,1]
    df.loc[df.str.contains(",")]=temp.loc[:,2]+' '+temp.loc[:,0]
    return df

def cleaning_data():
    df=pd.read_csv("src/presidents.tsv",sep='\t')
    df['President']=clean_names(df['President'])
    df['Vice-president']=clean_names(df['Vice-president'])
    
    
    df3=df['Start']
    df3=df3.str.split(" ",expand=True)
    df['Start']=df3[0].astype(int)

    df['Last']=df['Last'].where(df['Last'].str.isdigit())

    df['Seasons']=df['Seasons'].replace("two",2).astype(int)
    df = df.astype({"President" : object, "Start" : int,"Last": float,"Seasons":int,"Vice-president":object})    # different types for columns

    #print(df)
    
    return df

def main():
    print(cleaning_data())
    return

if __name__ == "__main__":
    main()
