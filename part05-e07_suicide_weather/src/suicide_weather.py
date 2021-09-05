#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df=pd.read_csv("src/who_suicide_statistics.csv")
    df['new']=df['suicides_no']/df['population']
    df=df.groupby('country').mean()
    df2=df['new']
    
    result=pd.DataFrame(df2)
    result.columns=['Average Temp']
    return result

def suicide_weather():
    page=pd.read_html("src/List_of_countries_by_average_yearly_temperature.html")
    page=page[0]
    page=page.set_index('Country')
    df=suicide_fractions()
    page.columns=['Average Temp']
    df.columns=['Average Temp']
    page = page.iloc[:, 0].str.replace("\u2212", "-").astype(float)

    #print(page.dtypes)

    df_new=pd.merge(df, page, left_index=True, right_index=True)
    #print(df_new.head())
    coeff=df_new.corr(method='spearman')

    return (df.shape[0], page.shape[0], df_new.shape[0], coeff.iloc[0,1])

def main():
    su,temp,com,sc=suicide_weather()
    print(f"Suicide DataFrame has {su} rows")
    print(f"Temperature DataFrame has {temp} rows")
    print(f"Common DataFrame has {com} rows")
    print(f"Spearman correlation: {sc}")

if __name__ == "__main__":
    main()
