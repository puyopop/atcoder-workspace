#!/usr/bin/env python3
import sys


def solve(N: int, l: "List[int]", r: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    l = [int()] * (N)  # type: "List[int]"
    r = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    print(solve(N, l, r))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
