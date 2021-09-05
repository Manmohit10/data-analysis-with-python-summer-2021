#!/usr/bin/env python3

from functools import reduce
import numpy as np

def matrix_power(a, n):
    #return reduce(np.matmul, (a for _ in range(n) ), np.eye(a.shape[0]))
    if n==0:
        return np.eye(a.shape[1])
    elif n>0:
        g=[a for i in range(n)]
        return reduce(lambda x,y:x@y,g)
    else:
        g=[np.linalg.inv(a) for i in range(n*(-1))]
        return reduce(lambda x,y:x@y,g)

def main():
    a=np.random.randint(-10,20,(4,4))
    print(matrix_power(a,-2)
    )


if __name__ == "__main__":
    main()
