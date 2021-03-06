#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, T: str):
    return YES if T[:-1] == S else NO


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    print(solve(S, T))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
