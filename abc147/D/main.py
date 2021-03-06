#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(N: int, A: "List[int]"):
    BN = 64
    B = [[0] * BN for _ in range(N+1)]
    for i, a in enumerate(A):
        for j in range(BN):
            B[i+1][j] = B[i][j] + ((a >> j) & 1)
    ans = 0
    for i in range(BN):
        b = 1 << i
        for j, a in enumerate(A):
            n = B[N][i] - B[j+1][i]
            if a & b:
                n = N - j  - n - 1
            ans = (ans + b * n % MOD) % MOD
    return ans


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
