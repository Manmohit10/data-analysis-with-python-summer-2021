#!/usr/bin/env python3


def main():
    for n in range(10):
        for m in range(10):
            print('{:>4}'.format((n+1)*(m+1)),end="")
        print("")

if __name__ == "__main__":
    main()
