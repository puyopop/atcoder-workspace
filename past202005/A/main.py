#!/usr/bin/env python3
import sys


def solve(s: str, t: str):
    if s == t:
        return 'same'
    if s.lower() == t.lower():
        return 'case-insensitive'
    return 'different'


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    print(solve(s, t))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
