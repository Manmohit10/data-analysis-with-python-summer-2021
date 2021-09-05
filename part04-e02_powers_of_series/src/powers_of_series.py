#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    df=pd.DataFrame(s, index=s.index,columns=[1])
    for i in range(k):
        if i==0:
            continue
        df[i+1]=s**(i+1)
    #    df = pd.DataFrame(dict(zip(range(1,k+1), c)))

    

    return df
    
def main():
    s = pd.Series([1,2,3,4,5,6], index=list("abcdef"))
    print(powers_of_series(s, 5))
    
if __name__ == "__main__":
    main()
