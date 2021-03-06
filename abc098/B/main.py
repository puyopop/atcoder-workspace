#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    h = [set()]
    for c in S:
        h.append(h[-1] | set(c))
    t = [set()]
    for c in reversed(S):
        t.append(t[-1] | set(c))
    return max(len(hh & tt) for hh, tt in zip(h, reversed(t)))

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    print(solve(N, S))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
