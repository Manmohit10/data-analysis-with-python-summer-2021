#!/usr/bin/env python3

def reverse_dictionary(d):
    dict1={}
    for key, value in d.items():
        for i in value:
            if i in dict1:
                print(i)
                dict1[i].append(key)
            else:
                print(i)
                dict1[i]=[key]
            
    return dict1

def main(): 
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'samosa'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))



if __name__ == "__main__":
    main()
