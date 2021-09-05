#!/usr/bin/env python3

import pandas as pd
from pandas.core.indexes.base import Index

def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv", sep='\t',index_col=['Region 2018'])
    df=df["Akaa":"Äänekoski"]
    return df
    
def main():
    pd.set_option('max_row', None)

    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
