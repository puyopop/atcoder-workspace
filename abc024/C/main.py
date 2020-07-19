#!/usr/bin/env python3
import sys


def solve(N: int, D: int, K: int, L: "List[int]", R: "List[int]", S: "List[int]", T: "List[int]"):
    p = S
    ans = [float('inf')] * K
    for d, (l, r) in enumerate(zip(L, R), 1):
        for i, pp in enumerate(p):
            if pp < l or r < pp:
                continue
            if S[i] < T[i]:
                p[i] = r
                if T[i] <= p[i]:
                    ans[i] = min(ans[i], d)
            else:
                p[i] = l
                if p[i] <= T[i]:
                    ans[i] = min(ans[i], d)                    
    return ans

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    L = [int()] * (D)  # type: "List[int]"
    R = [int()] * (D)  # type: "List[int]"
    for i in range(D):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    S = [int()] * (K)  # type: "List[int]"
    T = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
    print(*solve(N, D, K, L, R, S, T), sep='\n')

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()