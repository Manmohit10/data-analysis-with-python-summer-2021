#!/usr/bin/env python3

def interleave(*lists):
    temp=[]
    result=[]
    for i in lists:
        temp.append(i)
    for j in zip(*temp):
        result.extend(j)
    return result

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()