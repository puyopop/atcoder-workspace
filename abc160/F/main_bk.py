#!/usr/bin/env python3
import sys
import resource
sys.setrecursionlimit(2 * 10**5)
#resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))


MOD = 1000000007  # type: int

def solve(N: int, a: "List[int]", b: "List[int]"):
    ff = [1] * (N + 1)
    for i in range(1, N+1):
        ff[i] = (ff[i-1] * i) % MOD
    iff = [pow(ff[i], MOD-2, MOD) for i in range(N+1)]
    cache = {}
    def f(source, sink):
        key = (source, sink)
        if key in cache:
            return cache[key]
        c, ic, p = 0,1, 1
        for e in edges[sink]:
            if e == source:
                continue
            cc, pp = f(sink, e)
            p = (p * pp) % MOD
            c += cc
            ic = (ic * iff[cc]) % MOD
        cache[key] = c+1, p * (ff[c] * ic) % MOD
        return cache[key]

    def g(node):
        c, ic, p = 0, 1, 1
        for e in edges[node]:
            cc, pp = f(node, e)
            c += cc
            p = (p * pp) % MOD
            ic = (ic * iff[cc]) 
        return (((ff[c] * ic) % MOD) * p) % MOD
    
    edges = [[] for _ in range(N+1)]
    for aa, bb in zip(a, b):
        edges[aa].append(bb)
        edges[bb].append(aa)

    for i in range(1, N+1):
        print(g(i))


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

if __name__ == '__main__':
    main()