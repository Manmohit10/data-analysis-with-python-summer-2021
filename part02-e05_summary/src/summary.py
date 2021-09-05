#!/usr/bin/env python3

import sys
from math import sqrt

def summary(filename):
    num=[]
    with open(filename,"r") as f:
        for Line in f:
            try:
                num.append(float(Line))
            except:
                continue
        Sum=sum(num)
        L=len(num)
        avg=Sum/L
        sdtemp=[]
        sdtemp+=(((x-avg)**2) for x in num)
        stddev=sqrt(sum(sdtemp)/(L-1.0))    
    
    return (Sum,avg,stddev)

def main():
    for filename in sys.argv[1:]:
        s, a, stddev = summary(filename)
        print(f"File: {filename} Sum: {s:.6f} Average: {a:.6f} Stddev: {stddev:.6f}")

if __name__ == "__main__":
    main()
