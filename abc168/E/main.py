#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def func(b, w):
    return ((pow(2, b, MOD) + pow(2, w, MOD)) % MOD + MOD - 1) % MOD 

def solve(N: int, A: "List[int]", B: "List[int]"):
    from fractions import Fraction
    from collections import Counter
    C = [Fraction(a, b) for a, b in zip(A, B) if 0 not in (a, b)]
    D = [-Fraction(b, a) for a, b in zip(A, B) if 0 not in (a, b)]
    E = Counter(C)
    F = Counter(D)
    G = []
    used = set()
    for e, f in zip(E, F):
        if e in used or f in used:
            continue
        G.append((e, E[e], F[e]))
        used.add(e)
        used.add(f)
    ans = 1
    #print(G)
    for e, b, w in G:
        # print(b, w, func(b, w))
        ans = (ans * func(b, w)) % MOD
    H = sum(1 if 0 in (a, b) and (a!=0 or b!=0) else 0 for a, b in zip(A, B))
    print(ans)
    ans = (ans * func(H, 0)) % MOD
    return (ans-1+MOD)%MOD
        

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    print(solve(N, A, B))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
