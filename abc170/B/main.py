#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(X: int, Y: int):
    for i in range(X+1):
        if 2 * i + 4 * (X - i) == Y:
            return YES
    return NO


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    print(solve(X, Y))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
