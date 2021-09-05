#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

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
    df.drop('Päivämäärä',axis=1,inplace=True)
    df=pd.concat([df2,df],axis=1)
    df = df[df["Year"]==2017] #Limited to 2017 Year
    df = df.groupby(["Day","Month","Year"]).sum().reset_index() 
    df['Auroransilta']=df['Auroransilta'].astype(np.float64)
    return df


def cycling_weather():
    df=pd.read_csv("src/kumpula-weather-2017.csv")
    df2=split_date()
    #df_cycle['Total']=df_cycle.iloc[:,5:24].sum(axis=1,skipna=True)
    df_cycle=pd.merge(df,df2,left_on=['Year','m','d'],right_on=['Year','Month','Day'])
    df_cycle=df_cycle.drop(['m','d','Time','Time zone'],axis=1)
    df_cycle = df_cycle.fillna(method='ffill')
    df_cycle.reset_index()
    #print(df_cycle)
    return df_cycle

def cycling_weather_continues(station):
    cycle=cycling_weather()
    model=LinearRegression(fit_intercept=True)
    X = cycle[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = cycle[station]
    #print(cycle.head())
    model.fit(X,y)
    coeff=model.coef_   
    print(coeff)
    score=model.score(X,y)
    return ((coeff), score)
    
def main():
    station="Merikannontie"
    coeff,score=cycling_weather_continues(station)
    print(f"""Measuring station: {station}
Regression coefficient for variable 'precipitation': {coeff[0]:.1f}
Regression coefficient for variable 'snow depth': {coeff[1]:.1f}
Regression coefficient for variable 'temperature': {coeff[2]:.1f}
Score: {score:.2f}""")
    return

if __name__ == "__main__":
    main()
