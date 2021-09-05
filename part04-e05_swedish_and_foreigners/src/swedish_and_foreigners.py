#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep='\t',index_col=['Region 2018'])
    df=df["Akaa":"Äänekoski"]
    cols=df.columns
    df=df[df[cols[2]] > 5]
    df=df[df[cols[3]] > 5]    
    df=df[['Population','Share of Swedish-speakers of the population, %','Share of foreign citizens of the population, %']]
    return df
    

def main():
    #pd.set_option('max_columns', None)

    print(swedish_and_foreigners())
if __name__ == "__main__":
    main()
