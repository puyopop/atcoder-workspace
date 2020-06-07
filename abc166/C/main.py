#!/usr/bin/env python3
import sys


def solve(N: int, M: int, H: "List[int]", A: "List[int]", B: "List[int]"):
    mh = [-1] * N
    for a, b in zip(A, B):
        mh[a-1] = max(mh[a-1], H[b-1])
        mh[b-1] = max(mh[b-1], H[a-1])
    ans = 0
    for h, mhh in zip(H, mh):
        if h > mhh:
            ans += 1
    return ans


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    print(solve(N, M, H, A, B))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()