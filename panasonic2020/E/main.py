#!/usr/bin/env python3
import sys


def solve(a: str, b: str, c: str):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = next(tokens)  # type: str
    b = next(tokens)  # type: str
    c = next(tokens)  # type: str
    print(solve(a, b, c))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
