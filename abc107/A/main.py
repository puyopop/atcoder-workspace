#!/usr/bin/env python3
import sys


def solve(N: int, i: int):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    i = int(next(tokens))  # type: int
    print(solve(N, i))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
