#!/usr/bin/env python3

def extract_numbers(s):
    word = s.split()
    List=[]
    for l in word:
        try:
            List.append(int(l))
        except ValueError:
            try:    
                List.append(float(l))
            except ValueError:    
                continue

    return List

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
