#!/usr/bin/env python3
import sys


def solve(N: int, M: int, X: int, Y: int, a: "List[int]", b: "List[int]"):
    a.append(float('inf'))
    b.append(float('inf'))
    i, j, t = 0, 0, 0
    ans = 0
    while i < N or j < M:
        print(i, j)
        while t <= a[i] and i < N:
            i += 1
        t = a[i] + X
        while t <= b[j] and j < M:
            j += 1
        t = b[j] + Y
        ans += 1
    return ans - 1
        


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    print(solve(N, M, X, Y, a, b))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
