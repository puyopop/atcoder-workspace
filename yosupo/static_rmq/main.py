# ref:https://maspypy.com/segment-tree-%e3%81%ae%e3%81%8a%e5%8b%89%e5%bc%b71
class SegmentTree:
    def __init__(self, seq, X_unit, X_f):
        self.N = len(seq)
        self.X_f = X_f
        self.X_unit = X_unit
        self._build(seq)

    @classmethod
    def build(cls, N, X_unit, X_f):
        return cls([X_unit]*N, X_unit, X_f)
    
    def _build(self, seq):
        self.X = [None] * (self.N+self.N)
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i<<1], self.X[i<<1|1])

    def update(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i<<1], self.X[i<<1|1])
    
    def fold(self, l, r):
        l += self.N
        r += self.N
        vl = self.X_unit
        vr = self.X_unit
        while l < r:
            if l & 1:
                vl = self.X_f(vl, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                vr = self.X_f(self.X[r], vr)
            l >>= 1
            r >>= 1
        return self.X_f(vl, vr)

if __name__ == "__main__":
    N, Q = map(int, input().split())
    a = list(map(int, input().split()))
    st = SegmentTree(a, float("inf"), min)
    for _ in range(Q):
        l, r = map(int, input().split())
        print(st.fold(l, r))
