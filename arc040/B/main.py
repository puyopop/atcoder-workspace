#!/usr/bin/env python3
import sys


def solve(N: int, R: int, S: str):
    '''
    >>> solve(3, 1, "o.o")
    2
    >>> solve(3, 2, "o.o")
    1
    >>> solve(3, 10000, "o.o")
    1
    '''
    t = S.rfind(".")
    if t == -1:
        return 0
    c, i = max(t-R+1, 0), t
    while i >= 0:
        i = i - R
        c += 1
        while i >= 0 and S[i] == "o":
            i -= 1
    return c

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    print(solve(N, R, S))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()
    main()
