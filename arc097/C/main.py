#!/usr/bin/env python3
import sys


def solve(s: str, K: int):
    pool = set()
    for l in range(K):
        for i in range(0, len(s)-l):
            pool.add(s[i:i+l+1])
    return sorted(pool)[K-1]


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    print(solve(s, K))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
