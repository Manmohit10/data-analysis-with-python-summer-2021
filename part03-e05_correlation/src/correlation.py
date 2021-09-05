#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    df=load()
    p_length = df[:,2]
    s_length = df[:,0]
    new=scipy.stats.pearsonr(s_length,p_length)
    return new[0]

def correlations():
    """df=load()
    p_width = df[:,3]
    p_length = df[:,2]
    s_length = df[:,0]
    s_width = df[:,1]
    new=np.corrcoef([s_length,s_width,p_length,p_width])
    return new"""
    iris = load()
    temp = iris.T
    print(temp)
    return np.corrcoef(temp)

def main():
    df=load()
    p_width = df[:,[3]]
    p_length = df[:,[2]]
    s_length = df[:,[0]]
    s_width = df[:,[1]]
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
