#!/usr/bin/env python3

def main():
    for n in range(1,6):
        for m in range(1,6):
            if m+n==5:
                print(f"({n},{m})")

if __name__ == "__main__":
    main()
