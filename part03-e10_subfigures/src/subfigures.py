#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x=a[:,0]
    y=a[:,1]
    fig,ax=plt.subplots(1,2)
    ax[0].plot(x,y)
    ax[1].scatter(x,y,c=a[:,2],s=a[:,3])
    return plt.show()

    

def main():
    np.random.seed(1)
    a=np.random.randint(1,20,(16,4))
    print(a)
    subfigures(a)
    
    """a = np.concatenate([np.arange(n).reshape(n,1), a], axis=1)
        a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)"""

if __name__ == "__main__":
    main()
