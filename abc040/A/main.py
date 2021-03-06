#!/usr/bin/env python3
import sys


def solve(n: int, x: int):
    return min(x-1, n-x)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    print(solve(n, x))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
