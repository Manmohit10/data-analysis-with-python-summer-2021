#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    row=[]
    for i in range(a.shape[0]):
        row.append(a[i])
    return row

def get_columns(a):
    column=[]
    for i in range(a.shape[1]):
        column.append(a[:,i])
    return column

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
