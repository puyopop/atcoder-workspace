#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (Q)  # type: "List[int]"
    D = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    print(solve(N, Q, A, B, C, D))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
