#!/usr/bin/env python3
import sys


def solve(D: int, c: "List[int]", s: "List[List[int]]", t: "List[int]", M: int, d: "List[int]", q: "List[int]"):
    ans = 0
    lasts = [0] * 26
    sum_c = sum(c)
    daily_loss = sum_c
    adjusts = [[0] * (D+1) for _ in range(26)]
    for day, tt in enumerate(t, 1):
        a = s[day-1][tt-1]
        lasts[tt-1] = day
        for i in range(26):
            adjusts[i][day]=lasts[i]*c[i]
        a -= daily_loss
        a += sum(adjust[day] for adjust in adjusts)
        ans += a
        daily_loss += sum_c
    sum_a = [sum(adjust) for adjust in adjusts]
    for dd, qq in zip(d, q):
        fro, to = t[dd]-1, qq-1
        t[dd-1] = to
        fro_a, to_a = adjusts[fro][dd], adjusts[to][dd]
        for i in range(dd, D+1):
            if adjusts[fro][i] != fro_a:
                break
            adjusts[fro][i] = adjusts[fro][dd-1]
        for i in range(dd, D+1):
            if adjusts[to][i] != to_a:
                break
            adjusts[to][i] = dd * c[qq-1]
        ans -= sum_a[fro] + sum_a[to]
        sum_a[fro] = sum(adjusts[fro])
        sum_a[to] = sum(adjusts[to])
        ans += sum_a[fro] + sum_a[to]
        print(ans)


# https://kopricky.github.io/code/For_Python/bit.html
class BIT:
    def __init__(self, node_size):
        self._node = node_size+1
        self.bit = [0]*self._node
 
    def add(self, index, add_val):
        index += 1
        while index < self._node:
            self.bit[index] += add_val
            index += index & -index
 
    def sum(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= index & -index
        return res

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    c = [int(next(tokens)) for _ in range(26)]  # type: "List[int]"
    s = [[int(next(tokens)) for _ in range(26)] for _ in range(D)]  # type: "List[List[int]]"
    t = [int(next(tokens)) for _ in range(D)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    d = [int()] * (M)  # type: "List[int]"
    q = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        d[i] = int(next(tokens))
        q[i] = int(next(tokens))
    print(solve(D, c, s, t, M, d, q))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
