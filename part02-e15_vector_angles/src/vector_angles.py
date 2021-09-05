#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    x=np.sqrt(np.sum(X*X,axis=1))
    y=np.sqrt(np.sum(Y*Y,axis=1))
    num=np.sum(X*Y,axis=1)
    den=np.sqrt(x*x)*np.sqrt(y*y)
    print(num/den)
    return np.degrees(np.arccos(np.clip(num/den,-1,1)))

def main():
    X = np.array([[1, 4, 3, 7], [3, 2, 2, 1]])
    Y = np.array([[2, 7, 5, 2], [8, 5, 1, 0]])
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
