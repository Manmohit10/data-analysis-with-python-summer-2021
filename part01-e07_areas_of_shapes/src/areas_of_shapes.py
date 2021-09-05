#!/usr/bin/env python3

import math


def main():
    while True:
        shape=input("Choose a shape (triangle, rectangle, circle):")
        shape=str(shape)
        if shape=="":
            break
        elif shape=='triangle':
            base=float(input('Give base of the triangle:'))
            height=float(input('Give height of the triangle:'))
            print(f"The area is {base*height*0.5}")
        elif shape=='rectangle':
            base=float(input('Give width of the rectangle:'))
            height=float(input('Give height of the rectangle:'))
            print(f"The area is {base*height}")
        elif shape=='circle':
            radius=float(input('Give radius of the circle:'))
            print(f"The area is {math.pi*(radius**2)}")
        else:
            print('Unknown shape!') 


        
if __name__ == "__main__":
    main()
