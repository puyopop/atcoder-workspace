#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, K: int, M: int, A: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    print(solve(N, K, M, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
