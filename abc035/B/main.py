#!/usr/bin/env python3
import sys


def solve1(C):
    X = abs(C['U']-C['D'])
    Y = abs(C['L']-C['R'])
    return X + Y + C['?']

def solve2(C):
    X = abs(C['U']-C['D'])
    Y = abs(C['L']-C['R'])
    Z = X + Y - C['?']
    if Z > 0:
        return Z
    return abs(Z) % 2

def solve(S: str, T: int):
    from collections import Counter
    c = Counter(S)
    if T == 1:
        return solve1(c)
    return solve2(c)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = int(next(tokens))  # type: int
    print(solve(S, T))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
