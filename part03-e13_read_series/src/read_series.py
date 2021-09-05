#!/usr/bin/env python3
import pandas as pd

def read_series():
    df=pd.Series()
    a1=[]
    a2=[]
    while True:
        x=input("Enter values separated by string: ")
        if not x:
            break
        try :
            temp=x.split()
            if len(temp)>2:
                raise ValueError
            a2.append(temp[1])
            a1.append(temp[0])

        #df[temp[0]]=df[temp[1]]
        except :
            print("Retry")
            continue
    df=pd.Series(a2,index=a1)        

    return df

def main():
    a=read_series()
    print(a)
    

if __name__ == "__main__":
    main()
