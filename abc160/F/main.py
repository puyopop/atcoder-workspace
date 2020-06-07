#!/usr/bin/env python3
import sys
import resource
sys.setrecursionlimit(2 * 10**5)
#resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))


MOD = 1000000007  # type: int

def solve(N: int, a: "List[int]", b: "List[int]"):
    mf = ModFactorial(MOD, N)
    edges = [[] for _ in range(N)]
    for aa, bb in zip(a, b):
        edges[aa-1].append(bb-1)
        edges[bb-1].append(aa-1)
        
    sizes = [0] * N
    par = [None] * N
    def f(pre, cur):
        par[cur] = pre
        for n in edges[cur]:
            if pre == n:
                continue
            sizes[cur] += f(cur, n) + 1
        return sizes[cur]
    f(None, 0)

    dp1 = [None] * N
    def g(pre, cur):        
        a = mf.factorial(sizes[cur])
        for n in edges[cur]:
            if n == pre:
                continue
            a = a * g(cur, n) % MOD
            a = a * mf.factorial_inv(sizes[n]+1) % MOD
        dp1[cur] = a
        return a
    g(None, 0)

    dp2 = [None] * N
    dp2[0] = 1
    def h(cur):
        if dp2[cur]:
            return dp2[cur]
        a = dp1[par[cur]] #0
        a = a * mf.factorial(sizes[cur]+1) % MOD #1
        a = a * mf.factorial(N-sizes[cur]-2) % MOD #2
        a = a * h(par[cur]) % MOD #3
        a = a * mf.factorial_inv(sizes[par[cur]]) % MOD #4
        a = a * mf.factorial_inv(N-sizes[par[cur]]-1) % MOD #5
        a = a * mod_inv(MOD, dp1[cur]) % MOD #6
        dp2[cur] = a
        return a

    for i in range(N):
        a = dp1[i] * h(i) % MOD
        a = a * mf.factorial(N-1) % MOD
        a = a * mf.factorial_inv(sizes[i]) % MOD
        a = a * mf.factorial_inv(N - sizes[i] - 1) % MOD
        print(a)

def mod_range(mod, start, stop=None, step=1):    
    if stop == None:
        stop = start
        start = 0
    return map(lambda i: i % mod, range(start, stop, step))

def mod_inv(mod, n):
    '''
    >>> mod_inv(3, 2)
    2
    >>> mod_inv(1000000007, 2)
    500000004
    '''
    return pow(n, mod-2, mod)

class ModFactorial:
    def __init__(self, mod, size=1):
        '''
        >>> ModFactorial(7, 7)
        Traceback (most recent call last):
        ...
        AssertionError
        '''
        assert mod > size
        self._mod = mod
        self._init_factorials(size)

    def _mod_range(self, start, stop=None, step=1):
        return mod_range(self._mod, start, stop, step)
        
    def _init_factorials(self, size):
        '''
        >>> mf1 = ModFactorial(1000000007)
        >>> mf2 = ModFactorial(1000000007, 10)
        >>> mf1.factorial(10) == mf2.factorial(10)
        True
        '''
        self._factorials = [1] * size        
        n = 1 # リストの参照は遅いので減らす
        for i, m in enumerate(self._mod_range(1, size), 1):
            n = (n * m) % self._mod
            self._factorials[i] = n
            
    def _append_factorials(self, n):
        for m in map(lambda i: i % self._mod, range(len(self._factorials), n+1)):
            self._factorials.append((self._factorials[-1] * m) % self._mod)

    def _mod_inv(self, n):
        return mod_inv(self._mod, n)

    def factorial(self, n):
        '''
        >>> ModFactorial(1000000007).factorial(10)
        3628800
        >>> ModFactorial(7).factorial(6)
        6
        >>> ModFactorial(7).factorial(7)
        Traceback (most recent call last):
        ...
        AssertionError
        '''
        assert n < self._mod
        if len(self._factorials) <= n:
            self._append_factorials(n)
        return self._factorials[n]

    def factorial_inv(self, n):
        '''
        >>> MOD = 1000000007
        >>> mf = ModFactorial(MOD)
        >>> mf.factorial_inv(10)
        283194722
        >>> mf.factorial_inv(10) * mf.factorial(10) % MOD
        1
        >>> MOD = 7
        >>> mf = ModFactorial(MOD)
        >>> mf.factorial_inv(6)
        6
        >>> mf.factorial_inv(6) * mf.factorial(6) % MOD
        1
        '''
        return self._mod_inv(self.factorial(n))

    def permutation(self, n, r):
        '''
        >>> ModFactorial(1000000007).permutation(10, 2)
        90
        '''
        return self.factorial(n) * self.factorial_inv(n-r) % self._mod

    def combination(self, n, r):
        '''
        >>> ModFactorial(1000000007).combination(10, 2)
        45
        '''
        return self.permutation(n, r) * self.factorial_inv(r) % self._mod


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

if __name__ == '__main__':
    main()