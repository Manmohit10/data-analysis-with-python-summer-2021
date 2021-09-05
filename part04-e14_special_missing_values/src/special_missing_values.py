#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
from pandas.tseries.offsets import Second

def special_missing_values():
    df=pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    df=df.replace("New",np.nan).replace("Re",np.nan)
    df=df.dropna(axis=0)
    df['LW']=df['LW'].astype(int)
    df=df[df['Pos']>df['LW']]
    return df

def main():
    #print(os.getcwd())
    pd.set_option('max_columns', None)
    df=special_missing_values()
    print(df)

if __name__ == "__main__":
    main()
