#!/usr/bin/env python3


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    from itertools import repeat, chain
    from heapq import heappush, heappop, heapify
    N = int(input())
    qs = []
    for _ in range(N):
        t = map(int, input().split())
        next(t)
        for i, tt in enumerate(t):
            if len(qs) <= i:
                qs.append([])
            qs[i].append(tt)
    for i in range(N):
        qs[i].sort()
    M = int(input())
    st = SegmentTree(N, max, (0, 0))
    for i in range(N):
        st.update(i, (qs[i].pop(), i))
    print(st.dat)
    for a in map(int, input().split()):
        v, i = st.query(0, a)
        if qs[i]:
            st.update(i, (qs[i].pop(), i))
        else:
            st.update(i, (-float('inf'), i))
        print(v, st.dat)


def test():
    import doctest
    doctest.testmod()

# https://qiita.com/dn6049949/items/afa12d5d079f518de368
class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2-1) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size-1
        self.dat[i] = x
        while i > 0:
            i = (i-1) >> 1
            self.dat[i] = self.f(self.dat[i*2+1], self.dat[i*2+2])

    def query(self, l, r, k=0, L=0, R=None):
        if R is None:
            R = self.size
        if R <= l or r <= L:
            return self.default
        if l <= L and R <= r:
            return self.dat[k]
        else:
            lres = self.query(l, r, k*2+1, L, (L+R) >> 1)
            rres = self.query(l, r, k*2+2, (L+R) >> 1, R)
            return self.f(lres, rres)

if __name__ == '__main__':
    #test()
    main()
