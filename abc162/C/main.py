#!/usr/bin/env python3
import sys

def solve(K: int):
    from math import gcd
    from itertools import product
    from functools import reduce
    def f():
        for abc in product(range(1, K+1), repeat=3):
            yield reduce(gcd, abc)
    print(sum(f()))


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()
