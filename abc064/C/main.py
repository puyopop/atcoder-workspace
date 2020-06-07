#!/usr/bin/env python3
import sys

def f(r):
    '''
    >>> f(399)
    0
    >>> f(400)
    1
    >>> f(401)
    1
    >>> f(3200)
    8
    >>> f(3201)
    8
    '''
    from bisect import bisect
    R = [400, 800, 1200, 1600, 2000, 2400, 2800, 3200]
    return bisect(R, r)

def solve(N: int, a: "List[int]"):
    '''
    >>> solve(1, [399])
    (1, 1)
    >>> solve(1, [3200])
    (1, 1)
    >>> solve(1, [399, 388])
    (1, 1)
    >>> solve(1, [399, 3200])
    (1, 2)
    >>> solve(1, [399, 3200, 3200, 3400])
    (1, 4)
    >>> solve(1, [399, 400, 3200, 3200, 3400])
    (2, 5)
    >>> solve(1, [399, 400, 800, 1200, 1600, 2000, 2400, 3200, 3200, 3400])
    (7, 10)
    '''
    from collections import Counter
    b = tuple(map(f, a))
    c = Counter(b)
    return max(1, len(c)-(1 if c[8] else 0)), len(c)+(c[8]-1 if c[8] else 0)


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(*solve(N, a))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()
    main()