#!/usr/bin/env python3
import sys


def solve(N: int, M: int, a: "List[int]", b: "List[int]", t: "List[int]"):
    d = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for aa, bb, tt in zip(a, b, t):
        d[aa-1][bb-1] = tt
        d[bb-1][aa-1] = tt
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k]+d[j][k])
    return min(map(max, d))


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    t = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        t[i] = int(next(tokens))
    print(solve(N, M, a, b, t))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
