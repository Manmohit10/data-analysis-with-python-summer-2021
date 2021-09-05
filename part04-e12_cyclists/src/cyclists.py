#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df=pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    df[df.isnull().any(axis=1)]
    df=df.dropna(axis=1,how="all")
    df=df.dropna(axis=0,how="all")

    return df


def main():
    x=cyclists()
    print(x)
    return
    
if __name__ == "__main__":
    main()
