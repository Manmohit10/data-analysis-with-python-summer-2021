#!/usr/bin/env python3

import re

def file_extensions(filename):
    with open(filename,"r") as f:
        dct={}
        lst=[]  
        for line in f:
            line=line[:-1]
            #line=line.strip()
            #a=line.split(".")
            #b=line[-1]
            a=re.findall(r"\w*\.*\w*\.(.*)",line)
            if a==[]:
                lst.append(line)
            elif a[0] in dct:
                dct[a[0]].append(line)
            else:
                dct[a[0]]=[line]
                
    return (lst, dct)

def main():
    L,D=file_extensions("src/filenames.txt")
    sortednames=sorted(D.keys(), key=lambda x:x.lower())
    print(f"{len(L)} files with no extension")
    for i in sortednames:
        print(f"{i}{len(D[i])}")
        #for extension, files in sorted(d.items()):
        #print(f"{extension} {len(files)}"



if __name__ == "__main__":
    main()
