#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, l: "List[int]", r: "List[int]"):
    from collections import Counter
    c1 = Counter(l)
    c2 = Counter(r)
    f = 0
    ans = []
    for i in range(1, N+1):
        f += c1[i] - c2[i-1]
        ans.append(f%2)
    return ''.join(map(str, ans))


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    print(solve(N, Q, l, r))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
