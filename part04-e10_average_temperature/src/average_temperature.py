#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df=pd.read_csv("src/kumpula-weather-2017.csv")
    df=df[df['m']==7]
    avg=df['Air temperature (degC)'].mean()
    #print(df)
    return avg

def main():
    avg=average_temperature()
    print(f"Average temperature in July: {avg:.1f}")


if __name__ == "__main__":
    main()
