#!/usr/bin/env python3
import sys

NO = "Impossible"  # type: str

class Impossible(Exception):
    pass

def solve(N: int, M: int, a: "List[int]", x: "List[int]", y: "List[int]"):
    from heapq import heapreplace, heappop
    uf = UnionFind(N)
    for xx, yy in zip(x, y):
        uf.union(xx, yy)

    def f():
        aa = {r:iter(sorted(map(lambda x: a[x], m))) for r, m in uf.all_group_members().items()}
        roots = sorted(uf.roots(), reverse=True, key=lambda x: uf.size(x))
        god = uf.find(roots[0])
        hq = [(next(aa[god]), aa[god])]
        for r in roots[1:]:
            if len(hq) == 0:
                raise Impossible
            if uf.same(god, r):
                continue
            uf.union(god, r)
            s = hq[0]
            yield s[0]
            yield next(aa[r])
            try:
                heapreplace(hq, (next(aa[r]), aa[r]))
            except StopIteration:
                heappop(hq)
            try:
                heapreplace(hq, (next(s[1]), s[1]))
            except StopIteration:
                heappop(hq)

    try:
        print(list(f()))
        return sum(f())
    except Impossible:
        return NO

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N - 1 - 0 + 1)]  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    print(solve(N, M, a, x, y))

# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
        
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())

    def __iter__(self):
        return iter(range(self.n))
    
    def all_group_members(self):
        ret = {r:[] for r in self.roots()}
        for n in self:
            ret[self.find(n)].append(n)
        return ret
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

if __name__ == '__main__':
    main()
