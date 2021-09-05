#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df=pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    #print(df)
    clone=df.copy()
    df=df.replace("New",np.nan).replace("Re",np.nan)
    df=df.dropna(axis=0)
    df['LW']=df['LW'].astype(int)
    fil1=df['Pos']<df['LW']
    fil2=df['Pos']==df['Peak Pos']
    df['Peak Pos'].mask(fil1&fil2,np.nan,inplace=True)
    print(df['Peak Pos'])
    #print(df2)
    for i in range(40):
        try:
            clone.iloc[i]=df[df['LW']==(i+1)].iloc[0]    
        except:
            clone.iloc[i]=np.nan
    #print(clone)
    clone['Pos']=clone.index+1
    clone['LW']=np.nan
    clone['WoC']-=1


    return clone

def main():
    #pd.set_option('max_columns', None)
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    #print(df1)
    print(df['LW'].dtypes)
    #df['Pos']=df['LW']
    print(df)
    


if __name__ == "__main__":
    main()
