# 参考: https://qiita.com/drken/items/cce6fc5c579051e64fab
# Validation: https://atcoder.jp/contests/abc087/submissions/15381043
class UnionFind:
    def __init__(self, size: int):
        self.par = list(range(size))
        self.rank = [0] * size
        self.diff_weight = [0] * size

    def root(self, x: int):
        if self.par[x] == x:
            return x
        r = self.root(self.par[x])
        self.diff_weight[x] += self.diff_weight[self.par[x]] # 累積和をとる        
        #return par[x] := r
        self.par[x] = r
        return r

    def weight(self, x: int):
        self.root(x) # 経路圧縮
        return self.diff_weight[x]

    def same(self, x: int, y: int):
        return self.root(x) == self.root(y)

    # weight(y) - weight(x) = w となるように merge する
    def merge(self, x: int, y: int, w: int):
        # x と y それぞれについて、 root との重み差分を補正
        adjusted_w = w + self.weight(x) - self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:
            if adjusted_w != 0:
                raise MergeError
            return
        if self.rank[x] < self.rank[y]:
            x, y, adjusted_w = y, x, -adjusted_w
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self.diff_weight[y] = adjusted_w
