#!/usr/bin/env python3
import sys


def solve(N: int, h: "List[int]"):
    dp = [float('inf')] * (N+2)
    h.extend([0, 0])
    dp[0] = 0
    for i in range(N):
        dp[i+1] = min(dp[i+1], dp[i] + abs(h[i]-h[i+1]))
        dp[i+2] = min(dp[i+2], dp[i] + abs(h[i]-h[i+2]))
    return dp[N-1]

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, h))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
