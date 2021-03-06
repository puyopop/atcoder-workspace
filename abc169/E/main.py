#!/usr/bin/env python3
import sys

def solve(N: int, A: "List[int]", B: "List[int]"):
    from itertools import chain, repeat
    C = sorted(chain(zip(A, repeat(0)), zip(B, repeat(1))))
    ans = 0
    a, b, c = 0, 1, N-1
    for c1, c2 in zip(C, C[1:]):
        if (a + b) > c + 1:
            ans += c2[0] - c1[0]
        if c2[1] == 1:
            a, b, c = a + 1, b - 1, c
        if c2[1] == 0:
            a, b, c = a, b + 1, c - 1
    if N % 2 == 0:
        return ans * 2
    return ans

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    print(solve(N, A, B))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
