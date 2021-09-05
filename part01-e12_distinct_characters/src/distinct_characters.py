#!/usr/bin/env python3

def distinct_characters(L):
    dict1={}
    for i in L:
        dict1[i]=len(set(i))

    return dict1

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
