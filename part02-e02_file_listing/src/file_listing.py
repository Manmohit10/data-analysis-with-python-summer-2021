#!/usr/bin/env python3

import re

def file_listing(filename="src/listing.txt"):
    result=[]
    with open(filename, "r") as f:
        for line in f:
            r=re.findall(r'hyad-all\s*(\d*)\s*(\w*)\s*(\d*)\s*(\d*):(\d*)\s*([\w.]*)',line)
            l=[]
            for item in r[0]:
                try:
                    l.append(int(item))
                except (ValueError, TypeError):
                    l.append(item)
            t=tuple(l)
            result.append(t)
    return result

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
