#!/usr/bin/env python3
import sys


def solve(N: int, S: int, X: "List[int]", P: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        P[i] = int(next(tokens))
    print(solve(N, S, X, P))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
