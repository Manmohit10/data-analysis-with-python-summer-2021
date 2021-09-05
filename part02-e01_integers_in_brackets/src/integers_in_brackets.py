#!/usr/bin/env python3

import re
def integers_in_brackets(s):
    result=re.findall(r'\[\s*([+-]?\d*)\s*\]', s)
    return list(map(int,result))

def main():
    s1="afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"
    print(integers_in_brackets(s1))

if __name__ == "__main__":
    main()
