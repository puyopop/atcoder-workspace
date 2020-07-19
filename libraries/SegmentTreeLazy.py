# https://judge.yosupo.jp/submission/9146
class SegmentTreeLazy():
    def __init__(self, arr, ti, ei, func, op, merge):
        self.h = (len(arr) - 1).bit_length()
        self.n = 2**self.h
        self.func = func
        self.op = op
        self.merge = merge
        self.ti = ti
        self.ei = ei
        self.val = [ti for _ in range(2 * self.n)]
        for i in range(len(arr)):
            self.val[self.n + i] = arr[i]
        for i in range(1, self.n)[::-1]:
            self.val[i] = self.func(self.val[2 * i], self.val[2 * i + 1])
        self.laz = [ei for _ in range(2 * self.n)]

    def reflect(self, k):
        if self.laz[k] == self.ei:
            return self.val[k]
        return self.op(self.val[k], self.laz[k])

    def propagate(self, k):
        if self.laz[k] == self.ei: return
        self.laz[2 * k] = self.merge(self.laz[2 * k], self.laz[k])
        self.laz[2 * k + 1] = self.merge(self.laz[2 * k + 1], self.laz[k])
        self.val[k] = self.reflect(k)
        self.laz[k] = self.ei

    def thrust(self, k):
        for i in range(1, self.h + 1)[::-1]:
            self.propagate(k >> i)

    def recalc(self, k):
        while k:
            k >>= 1
            self.val[k] = self.func(self.reflect(2 * k), self.reflect(2 * k + 1))

    def update(self, lt, rt, x):
        lt += self.n
        rt += self.n
        vl = lt
        vr = rt
        self.thrust(lt)
        self.thrust(rt - 1)
        while rt - lt > 0:
            if lt & 1:
                self.laz[lt] = self.merge(self.laz[lt], x)
                lt += 1
            if rt & 1:
                rt -= 1
                self.laz[rt] = self.merge(self.laz[rt], x)
            lt >>= 1
            rt >>= 1
        self.recalc(vl)
        self.recalc(vr - 1)

    def query(self, lt, rt):
        lt += self.n
        rt += self.n
        self.thrust(lt)
        self.thrust(rt - 1)
        vl = vr = self.ti
        while rt - lt > 0:
            if lt & 1:
                vl = self.func(vl, self.reflect(lt))
                lt += 1
            if rt & 1:
                rt -= 1
                vr = self.func(self.reflect(rt), vr)
            lt >>= 1
            rt >>= 1
        return self.func(vl, vr)
