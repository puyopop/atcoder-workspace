#!/usr/bin/env python3
import sys
# from scipy.special import comb
sys.setrecursionlimit(10**4)
from math import factorial

def comb(n, r):
    '''
    >>> comb(2, 1)
    2
    >>> comb(3, 2)
    3
    '''
    if r == 0:
        return 1
    if n == 0 or r > n:
        return 0
    return factorial(n) // factorial(n - r) // factorial(r)

def f(S, i, k):
    # ここに来るのは繰り下がりが発生していない状態...
    if k == 0:
        # 以降は0を選び続けるしかない
        return 1
    if len(S) <= i:
        # 走破したのにK個使いきれていない
        return 0
    n = int(S[i])
    if n == 0:
        # 注目する桁が0の場合、0を選ぶしかない
        return f(S, i+1, k)
    # 注目する桁の数値nより小さい値を選べば、以降は繰り下げで選び放題
    ret = (n - 1) * comb(len(S)-i-1, k-1) * pow(9, k-1)
    ret += comb(len(S)-i-1, k) * pow(9, k)
    # 注目する桁の数値nを選んだ場合、繰り下げができない状態が続行    
    ret += f(S, i+1, k-1)
    return ret

def solve(S: str, K: int):
    return f(S, 0, K)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    print(solve(N, K))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()
    main()
