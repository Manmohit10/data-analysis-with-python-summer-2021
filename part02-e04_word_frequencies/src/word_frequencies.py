#!/usr/bin/env python3

def word_frequencies(filename):
    with open(filename,"r") as f:
        Result={}
        for line in f:
            lst=list(map(lambda x:x.strip("""!"#$%&'()*,-./:;?@[]_"""),line.split()))
            for word in lst:
                if word in Result:
                    Result[word]+=1
                else:
                    Result[word]=1
            

    return Result

def main():
    for word, count in word_frequencies("src/alice.txt").items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
