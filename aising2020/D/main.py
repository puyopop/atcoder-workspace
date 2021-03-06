#!/usr/bin/env python3
import sys


def solve(N: int, X: str):
    from itertools import product
    from collections import defaultdict, Counter
    ans = defaultdict(int)
    def f(x_y_z):
        x, y, z = x_y_z
        return x * x + y * y + z * z + x * y + y * z + z * x
    c = Counter(map(f, product(range(1, 101), repeat=3)))    
    return [c[i] for i in range(1, N+1)]

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = next(tokens)  # type: str
    print(*solve(N, X), sep="\n")

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
