#!/usr/bin/env python3

import pandas as pd

def top_bands():
    df1=pd.read_csv("src/bands.tsv",sep='\t')
    df2=pd.read_csv("src/UK-top40-1964-1-2.tsv",sep='\t')
    print(df1.head())
    print(df2.head())
    df1['Band']=df1['Band'].str.capitalize()
    df2['Artist']=df2['Artist'].str.capitalize()
    df_new=pd.merge(df1,df2,right_on="Artist",left_on="Band")
    return df_new

def main():
    print(top_bands())

if __name__ == "__main__":
    main()
