#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]", E: "List[int]", F: "List[int]"):
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    C = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    D = [int()] * (M)  # type: "List[int]"
    E = [int()] * (M)  # type: "List[int]"
    F = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        D[i] = int(next(tokens))
        E[i] = int(next(tokens))
        F[i] = int(next(tokens))
    print(solve(N, M, A, B, C, D, E, F))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
