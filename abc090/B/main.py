#!/usr/bin/env python3
import sys


def f(n):
    '''
    >>> f(1)
    True
    >>> f(2)
    True
    >>> f(22)
    True
    >>> f(34)
    False
    >>> f(565)
    True
    >>> f(789)
    False
    '''
    def g(n, m):
        return n // m % 10

    head = tail = 1
    while n // head > 10:
        head *= 10
    while head >= tail:
        if g(n, head) != g(n, tail):
            return False
        head //= 10
        tail *= 10
    return True

def solve(A: int, B: int):
    return sum(map(f, range(A, B+1)))

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
