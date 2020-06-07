#!/usr/bin/env python3


def main():
    r, D, x = list(map(int, input().split()))
    for _ in range(10):
        x = r * x - D
        print(x)

if __name__ == '__main__':
    main()
