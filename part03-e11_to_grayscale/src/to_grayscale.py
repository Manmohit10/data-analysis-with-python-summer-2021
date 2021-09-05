#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    """avg=np.array([0.2126,0.7152,0.0722 ]).reshape(1,3)
    new=image*avg
    new=new.sum(axis=2)"""
    avg=[0.2126,0.7152,0.0722]
    new=np.sum(image*avg, axis=2)
    return new

def to_red(image):
    m=[1,0,0]
    new=image*m
    return new

def to_green(image):
    m=[0,1,0]
    new=image*m
    return new

def to_blue(image):
    m=[0,0,1]
    new=image*m
    return new

def main():
    painting=plt.imread("src/painting.png")
    plt.subplot(3,1,1)
    red=to_red(painting)
    plt.imshow(red)

    plt.subplot(3,1,2)
    green=to_green(painting)
    plt.imshow(green)

    plt.subplot(3,1,3)
    red=to_blue(painting)
    plt.imshow(red)

    plt.show()

    new = to_grayscale(painting)
    plt.gray()
    plt.imshow(new)
    plt.show()


if __name__ == "__main__":
    main()
