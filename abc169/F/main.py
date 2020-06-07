#!/usr/bin/env python3
import sys
sys.setrecursionlimit(5000)

MOD = 998244353  # type: int

cache = [[None] * (3000+1) for _ in range(3000+1)]

def f(s, i, A, N):
    if s < 0:
        return 0
    if i == N:
        if s == 0:
            return 1
        return 0
    if cache[i][s] is not None:
        return cache[i][s]
    ret = (2 * f(s, i+1, A, N) % MOD + f(s-A[i], i+1, A, N)) % MOD
    cache[i][s] = ret
    return ret

def solve(N: int, S: int, A: "List[int]"):
    return f(S, 0, A, N)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, S, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()