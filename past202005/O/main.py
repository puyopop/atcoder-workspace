#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]", R: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    R = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    print(solve(N, M, A, B, R))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()