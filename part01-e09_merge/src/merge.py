#!/usr/bin/env python3

def merge(L1, L2):
    len1=len(L1)
    len2=len(L2)
    mlist=[]
    m=0
    n=0
    p=0
    q=0
    for i in range(len1):
        if p or q == 1:
            break
        for j in range(len2):
            if L1[m]<L2[n]:
                mlist.append(L1[m])
                m=m+1
                if m==len1:
                    m=m-1
                    p=1
            else:
                mlist.append(L2[n])
                n=n+1
                if n>=len2:
                    n=n-1
                    q=1
            if p or q ==1:
                break
    if(p==0):
        return mlist+L1[m:]
    else:
        return mlist+L2[n:]         


def main():
    L1 = [1,5,9,12]
    L2 = [2,6,10]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()