#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    def f(n):
        res = 0
        while n % 2 == 0:
            n //= 2
            res += 1
        return res
    return sum(map(f, a))


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, a))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
