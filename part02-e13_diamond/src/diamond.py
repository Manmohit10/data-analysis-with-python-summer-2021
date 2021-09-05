#!/usr/bin/env python3

import numpy as np

def diamond(n):
    eye=np.eye(n,dtype=int)
    new1=np.concatenate((np.flip(eye,1),eye),axis=1)
    new2=np.concatenate((new1,np.flip(new1,0)),axis=0)
    final = np.delete(new2,n,0)
    final = np.delete(final,n,1)
    #e=np.eye(n, dtype=int)
    #a=np.concatenate([e[::-1], e[:,1:]], axis=1)
    #result = np.concatenate([a[:-1], a[::-1]], axis=0)


    return final

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()
