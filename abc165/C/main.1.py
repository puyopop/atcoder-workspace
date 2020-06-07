#!/usr/bin/env python3
import sys

def solve(N: int, M: int, Q: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    from itertools import combinations_with_replacement
    def f(s):
        ret = 0
        for aa, bb, cc, dd in zip(a, b, c, d):
            if s[bb-1] - s[aa-1] == cc:
                ret += dd
        return ret
    return max(map(f, combinations_with_replacement(range(1, M+1), N)))


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (Q)  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    c = [int()] * (Q)  # type: "List[int]"
    d = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    print(solve(N, M, Q, a, b, c, d))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
