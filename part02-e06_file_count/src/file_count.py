#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename,"r") as f:
        NoofLines=0
        NoofWords=0
        NoofChar=0
        for line in f:
            NoofLines+=1
            lst=list(line.split())
            NoofWords=NoofWords+len(lst)
            NoofChar=NoofChar+len(line)
    return (NoofLines,NoofWords,NoofChar)

def main():
    for i in sys.argv[1:]:
        LC,WC,CC = file_count(i)
        print(f"{LC}\t{WC}\t{CC}\t{i}")

if __name__ == "__main__":
    main()
