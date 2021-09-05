#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df=pd.read_csv("src/kumpula-weather-2017.csv")
    df=df[df['Year']==2017]
    max=df['Snow depth (cm)'].max()
    #print(df)
    return max

def main():
    depth=snow_depth()
    print(depth)
    print(f"Max snow depth: {depth:.1f}")

    return

if __name__ == "__main__":
    main()
