#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    print(solve(N, a, b, c))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
