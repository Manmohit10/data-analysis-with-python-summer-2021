#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    x,y=a.shape[:2]

    return x/2-0.5,(y-1)/2   # note the order: (center_y, center_x)

def radial_distance(a):
    x,y=a.shape[:2]
    x,y=int(x),int(y)

    new=np.empty((1,int(y)))
    x1,y1=center(a)
    for i in range(x):
        list=[]
        for j in range(y):
            list.append(np.sqrt((i-x1)**2+(j-y1)**2))
        temp=np.array(list).reshape(1,y)
        new=np.append(new,temp,axis=0)
    new=np.delete(new,0,0)
    return new
    """
    Y = np.full((w, h), range(h)).T
    X = np.full((h, w), range(w))
    return np.sqrt((Y-y)**2 + (X-x)**2)"""

def scale(a, tmin=0.0, tmax=1.0):
    p1=(a-np.min(a))/(np.max(a)-np.min(a))
    p2=p1*(tmax-tmin)
    b=(a-np.min(a))/(np.max(a)-np.min(a))*(tmax-tmin)
    """Returns a copy of array 'a' with its values scaled to be in the range 
    [tmin,tmax]"""
    return p2
    # return np.interp(a, (a.min(), a.max()), (tmin, tmax))

def radial_mask(a):
    #return scale(1 - radial_distance(a))
    s = radial_distance(a)
    if s.shape[0] <= 2 or s.shape[1] <= 2:
        return np.ones(s.shape)
    mask = scale(s)
    return 1 - mask


def radial_fade(a):
    x,y=a.shape[:2]
    temp=radial_mask(a).reshape(x,y,1)
    return a*temp

def main():
    image=plt.imread("src/painting.png")
    b=radial_distance(image)


    plt.subplot(3,1,1)
    plt.imshow(image)

    plt.subplot(3,1,2)
    rad=radial_mask(image)
    print(rad.shape)
    plt.imshow(rad)

    plt.subplot(3,1,3)
    rad_new=radial_fade(image)
    plt.imshow(rad_new)
    plt.show()
    
    


if __name__ == "__main__":
    main()
