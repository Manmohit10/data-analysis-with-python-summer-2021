#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    sh=int(a.shape[1]/2)
    b=np.sum(a[:,0:sh],axis=1)
    c=np.sum(a[:,sh:2*sh],axis=1)
    temp=b>c
    return a[temp]

def main():
    np.random.seed(3)
    a=np.random.randint(1,35,(4,6))
    print(a)
    print(first_half_second_half(a))
    pass

if __name__ == "__main__":
    main()
