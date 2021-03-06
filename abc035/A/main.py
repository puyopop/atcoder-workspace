#!/usr/bin/env python3
import sys


def solve(W: int, H: int):
    if H * 4 == W * 3:
        return '4:3'
    return '16:9'


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    print(solve(W, H))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
