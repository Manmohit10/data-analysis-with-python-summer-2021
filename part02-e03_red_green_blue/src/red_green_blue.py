#!/usr/bin/env python3

import re
from typing import List

def red_green_blue(filename="src/rgb.txt"):
    i=0
    List=[]
    with open(filename,"r") as f:
        rd=f.readlines()
        for line in rd:
            if i==0:
                i+=1
                continue
            r=re.findall(r"\s*(\d*)\s*(\d*)\s*(\d*)\s*(.*)",line)
            List.append(r[0][0]+"\t"+r[0][1]+"\t"+r[0][2]+"\t"+r[0][3])

            
            
    return List


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
