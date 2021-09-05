#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df=pd.read_csv("src/kumpula-weather-2017.csv")
    df=df[df['Air temperature (degC)']<0]
    nos=df['d'].count()
    #print(df)
    return nos

def main():
    temp=below_zero()
    print(f"Number of days below zero: {temp}")
if __name__ == "__main__":
    main()
