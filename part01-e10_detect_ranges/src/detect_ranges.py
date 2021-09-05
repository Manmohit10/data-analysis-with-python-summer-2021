#!/usr/bin/env python3

def detect_ranges(L):
    length=len(L)
    L = sorted(L)
    result=[]
    i=1
    k=0
    j=0
    while i < length:
        if L[i]-L[i-1]==1:
            k=0
            j=i
            while j<length:
                if L[j]-L[j-1]==1:
                    k+=1 
                    j+=1
                else:
                    result.append((L[i-1],L[i-1]+k+1))
                    i=i+k+1
                    break
            if j==length:
                result.append((L[i-1],L[i-1]+k+1))
                i=j+1
        else:
            result.append(L[i-1])
            i+=1
        if i==length:
            result.append((L[i-1]))

    return result

def main():
    L = [2,5,4,8,12,6,7,10,13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
