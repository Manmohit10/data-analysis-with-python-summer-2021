#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    L1=s.index
    L2=s.values
    new=pd.Series(L1,L2)
    return new

def main():
    a=pd.Series([1, 4, 5, 2, 5, 2], index=list("abcdef"))
    print(inverse_series(a))


if __name__ == "__main__":
    main()
