#!/usr/bin/env python3
import sys


def solve_iter(N: int, A: "List[int]"):
    from collections import Counter
    def f(n):
        return n * (n - 1) // 2
    c = Counter(A)
    base = sum(map(f, c.values()))
    for a in A:
        yield base - f(c[a]) + f(c[a]-1)

def solve(N: int, A: "List[int]"):
    return list(solve_iter(N, A))

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(*solve(N, A), sep='\n')

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
