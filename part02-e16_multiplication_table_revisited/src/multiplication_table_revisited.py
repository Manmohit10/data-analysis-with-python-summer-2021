#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    zer=np.zeros((n,n),dtype=int)
    row=np.arange(n).reshape(n,1)
    col=np.arange(n)[:np.newaxis]
    return row*col 
    """a=np.arange(n)
    print(a[:, np.newaxis])
    return a[:, np.newaxis] * a[np.newaxis, :]"""

def main():
    print(multiplication_table(3))

if __name__ == "__main__":
    main()
