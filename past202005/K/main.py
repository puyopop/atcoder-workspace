#!/usr/bin/env python3
import sys

def solve(N: int, Q: int, f: "List[int]", t: "List[int]", x: "List[int]"):
    par = [-i for i in range(N+1)]
    head = [i for i in range(N+1)]
    for ff, tt, xx in zip(f, t, x):
        tmp = head[tt]
        head[tt] = head[ff]
        head[ff] = par[xx]
        par[xx] = tmp
    for _ in range(100):
        for i in range(1, N+1):
            if par[i] < 0:
                continue
            par[i] = par[par[i]]
    for i in range(1, N+1):
        print(-par[i])

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    f = [int()] * (Q)  # type: "List[int]"
    t = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        f[i] = int(next(tokens))
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, Q, f, t, x)

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
