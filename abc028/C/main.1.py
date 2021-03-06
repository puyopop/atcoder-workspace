#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, D: int, E: int):
    from itertools import combinations
    F = [A, B, C, D, E]
    return sorted(map(sum, combinations(F, 3)))[-3]


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    print(solve(A, B, C, D, E))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
