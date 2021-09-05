/usr/bin/env python3

import pandas as pd

def best_record_company():
    df=pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    df1=df.groupby('Publisher')['WoC'].sum().sort_values(ascending=False)
    arg=df1.index[0]
    df2=df.loc[df['Publisher']==arg]
    return df2

def main():
    a=best_record_company()
    print(a)
    

if __name__ == "__main__":
    main()
