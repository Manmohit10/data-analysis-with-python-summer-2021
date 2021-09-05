#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df=pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    df[df.isnull().any(axis=1)]
    df=df.dropna(axis=1,how="all")
    df=df.dropna(axis=0,how="all")
    df2=df['Päivämäärä']
    cols=['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df2=df2.str.split(expand=True)
    df2.columns=cols
    df2['Hour']=df2['Hour'].str.split(":").str[0]
    df2['Weekday']=df2['Weekday'].replace("ma","Mon").replace("ti","Tue").\
        replace("ke","Wed").replace("to","Thu").replace("pe","Fri").\
        replace("la","Sat").replace("su","Sun")
    li1=['tammi','helmi','maalis','huhti','touko','kesä','heinä','elo','syys','loka','marras','joulu']
    li2=pd.Series(np.arange(1,13))
    di=dict(zip(li1,li2))
    df2['Month']=df2['Month'].map(di)
    df2 = df2.astype({"Day" : int, "Year" : int,"Hour":int})    # different types for columns


    return df2

def main():
    result=split_date()
    print(result.dtypes)
       
if __name__ == "__main__":
    main()
