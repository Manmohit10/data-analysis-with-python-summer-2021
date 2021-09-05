#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    b=a[:,[c]]
    print("b=",b)
    b.sort(axis=0)
    b=np.unique(b,return_counts=True)
    print("b2=",b)
    di={}
    for i in range(len(b[0])):
        di[b[0][i]]=b[1][i]
    dic=sorted(di.items(), key=lambda x: x[1],reverse=True)
    l=np.shape(a)
    d=np.empty([l[0],l[1]])
    j=0
    for i in range(len(b[0])):
        for row in a:
            if row[c]==dic[i][0]:
                d[j]=row
                j+=1
    return d

def main():
    np.random.seed(1)
    a=np.random.randint(1,10,(8,5))
    print("a=",a)
    print(most_frequent_first(a,0))


if __name__ == "__main__":
    main()
