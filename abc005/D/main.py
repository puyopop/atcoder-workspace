#!/usr/bin/env python3
import sys

class Acc2d:
    def __init__(self, array2d):
        h, w = len(array2d), len(array2d[0])
        hh, ww = h + 1, w + 1
        self.acc_table = [[0] * ww for _ in range(hh)]
        for i in range(1, hh):
            for j in range(1, ww):
                self.acc_table[i][j] = self.acc_table[i-1][j] + self.acc_table[i][j-1] - self.acc_table[i-1][j-1] + array2d[i-1][j-1]

    def calc_sum(self, pos1, pos2):
        x, y = pos1
        xx, yy = pos2
        return self.acc_table[xx][yy] - self.acc_table[xx][y] - self.acc_table[x][yy] + self.acc_table[x][y]

    def __str__(self):
        return '\n'.join(map(str, self.acc_table))

def solve(N: int, D: "List[List[int]]", Q: int, P: "List[int]"):
    from itertools import combinations, product
    acc2d = Acc2d(D)
    H, W = len(D), len(D[0])
    ma = [0] * (H * W  + 1)
    f = lambda p1, p2: (p1[0]-p2[0])*(p1[1]-p2[1])
    for p1, p2 in combinations(product(range(H+1), range(W+1)), 2):
        a = f(p1, p2)
        if a <= 0:
            continue
        ma[a] = max(ma[a], acc2d.calc_sum(p1, p2))
    for i in range(1, len(ma)):
        ma[i] = max(ma[i-1], ma[i])
    return [ma[p] for p in P]


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    Q = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    print(*solve(N, D, Q, P), sep='\n')

if __name__ == '__main__':
    main()
