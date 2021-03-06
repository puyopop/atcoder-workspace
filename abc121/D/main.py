#!/usr/bin/env python3
import sys


def f(n):
    '''
    >>> f(1)
    1
    >>> f(6)
    7
    '''
    return (0 if n % 2 else n) ^ (1 if (n+1) // 2 % 2 else 0)


def solve(A: int, B: int):
    return f(A-1) ^ f(B)


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    print(solve(A, B))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()
    main()
