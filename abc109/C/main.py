#!/usr/bin/env python3
import sys


def solve(N: int, X: int, x: "List[int]"):
    from fractions import gcd
    from functools import reduce
    return reduce(gcd, [abs(xx-X) for xx in x])


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, X, x))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
