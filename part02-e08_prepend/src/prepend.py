#!/usr/bin/env python3

class Prepend(object):
    """new class"""
    def __init__(self,S):
        self.start=S
    def write(self,st):
        print(self.start+st)

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
