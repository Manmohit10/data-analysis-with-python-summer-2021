#!/usr/bin/env python3

def triple (a):
    """multiply by 3"""
    trip=a*3
    return trip
def square(b):
    """squared"""
    sq=b**2
    return sq

def main():
    for i in range(1,11):
        a=square(i)
        b=triple(i)
        if a>b:
            break
        else:
            print(f"triple({i})=={b} square({i})=={a}")
    
    

if __name__ == "__main__":
    main()
