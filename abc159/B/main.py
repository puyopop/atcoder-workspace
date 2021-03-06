#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def is_pal(s):
    return s == s[::-1]

def solve(S: str):
    N = len(S)
    return YES if is_pal(S) and is_pal(S[:N//2]) and is_pal(S[N//2+1:]) else NO


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    print(solve(S))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
