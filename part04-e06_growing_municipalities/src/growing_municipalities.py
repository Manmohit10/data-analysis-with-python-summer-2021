#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    df1=df[df['Population change from the previous year, %']>0]
    result = len(df1)/len(df)
    return result

def main():
    df = pd.read_csv("src/municipal.tsv", sep='\t',index_col=['Region 2018'])
    df=df["Akaa":"Äänekoski"]
    #df=df[10:20]
    pd.set_option('max_columns', None)
    print(df[['Population','Population change from the previous year, %']])
    ans=growing_municipalities(df)
    print(f"Proportion of growing municipalities: {ans:.1%}")

if __name__ == "__main__":
    main()
