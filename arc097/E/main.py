#!/usr/bin/env python3
import sys


def solve(N: int, c: "List[str]", a: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    c = [str()] * (2 * N)  # type: "List[str]"
    a = [int()] * (2 * N)  # type: "List[int]"
    for i in range(2 * N):
        c[i] = next(tokens)
        a[i] = int(next(tokens))
    print(solve(N, c, a))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()