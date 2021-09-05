#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    b=a[:,1]
    c=a[:,-2]
    d=b>c
    return a[d]
    
def main():
    np.random.seed(2)
    a=np.random.randint(1,50,(5,4))
    print(a)
    print(column_comparison(a))

if __name__ == "__main__":
    main()
