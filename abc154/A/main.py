#!/usr/bin/env python3
import sys


def solve(S: str, T: str, A: int, B: int, U: str):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    U = next(tokens)  # type: str
    print(solve(S, T, A, B, U))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
