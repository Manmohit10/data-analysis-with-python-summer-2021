#!/usr/bin/env python3
from numpy import delete
import pandas as pd

def create_series(L1, L2):
    indices=['a','b','c']
    s1=pd.Series(L1,indices)
    s2=pd.Series(L2,indices)
    return s1,s2
    
def modify_series(s1, s2):
    s1['d']=s2['b']
    s2=s2.drop('b',axis=0)
    return (s1,s2)
    
def main():
    a,b=create_series([1,2,3],[5,6,7])
    print(a)
    print(b)
    c,d=modify_series(a,b)
    print(c)
    print(d)
    print(c+d)
    
if __name__ == "__main__":
    main()
