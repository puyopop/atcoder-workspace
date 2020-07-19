#!/usr/bin/env python3
import sys

def solve(N: int, M: int):
    for s in range(2):
        m = M - 3 * s
        if m < 0 or m % 2:
            continue
        # 大人で賄えない分は赤ん坊で賄う
        b = max(m // 2 - (N - s), 0)
        a = N - b - s 
        if a < 0 or 2 * a + 3 * s + 4 * b != M:
            continue
        return a, s, b
    return -1, -1, -1

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    print(*solve(N, M))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()
    main()