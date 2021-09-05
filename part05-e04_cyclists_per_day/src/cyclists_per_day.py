#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    df2 = df2.astype({"Day" : int, "Year" : int,"Hour":int,"Month":int})    # different types for columns
    
    return df,df2


def split_date_continues():
    df,df2=split_date()
    df.drop('Päivämäärä',axis=1,inplace=True)
    df=pd.concat([df2,df],axis=1)
    df['Auroransilta']=df['Auroransilta'].astype(np.float64)
    return df

def cyclists_per_day():
    df=split_date_continues()
    df.drop(['Weekday','Hour'],axis=1,inplace=True)
    df=df.groupby(["Year","Month","Day"]).sum()
    #print(df)
    return df
    
def main():
    #pd.set_option('max_columns', None)
    daily=cyclists_per_day()
    daily=daily.dropna()
    daily['Total']=daily.sum(axis=1,skipna=True)
    Aug2017=daily.loc[(2017,8,1):(2017,8,31)]
    #print(Aug2017)
    X=np.arange(1,32)
    print(X)
    plt.plot(X,Aug2017['Total'])
    plt.show()

    #print(daily)
    return

if __name__ == "__main__":
    main()
