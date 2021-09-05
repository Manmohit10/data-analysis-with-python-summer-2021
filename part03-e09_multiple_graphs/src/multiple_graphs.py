#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    x1=[2,4,6,7]
    y1=[4,3,5,1]
    x2=[1,2,3,4]
    y2=[4,2,3,1]
    """plt.plot([2,4,6,7], [4,3,5,1], [1,2,3,4], [4,2,3,1])"""
    ax1=plt.plot(x1,y1)
    ax2=plt.plot(x2,y2)
    plt.xlabel("x axis")
    plt.ylabel("y label")
    plt.title("First Graph")
    plt.show()

if __name__ == "__main__":
    main()
