#!/usr/bin/env python3

import numpy as np

#import scipy.linalg

def vector_lengths(a):
    #return np.sqrt(np.sum(a**2, axis=1))
    sqrd=a*a
    sum=sqrd.sum(axis=1)
    result=np.sqrt(sum)
    return result

def main():
    a=np.arange(6).reshape(2,3)
    print((vector_lengths(a)))
    

if __name__ == "__main__":
    main()
