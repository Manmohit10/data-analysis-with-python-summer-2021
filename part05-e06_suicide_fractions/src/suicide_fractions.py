#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df=pd.read_csv("src/who_suicide_statistics.csv")
    df['new']=df['suicides_no']/df['population']
    df=df.groupby('country').mean()
    df2=df['new']

    return df2

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
