#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, M: int):
    factors = {}
    m = M
    for i in range(2, int(M**0.5)+1):
        while m % i == 0:
            factors[i] = factors.get(i, 0) + 1
            m //= i
    else:
        if m != 1:
            factors[m] = 1
    mf = ModFactorial(MOD)
    ans = 1
    for c in factors.values():
        ans = ans * mf.combination(c+N-1, c) % MOD
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
    print(solve(N, M))

def test():
    import doctest
    doctest.testmod()


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

def mod_permutation(mod, n, r):
    '''
    >>> mod_permutation(1000000007, 10, 2)
    90
    >>> mod_permutation(7, 10, 2)
    6
    '''
    m = 1
    for i in mod_range(mod, n-r+1, n+1):
        m = (m * i) % mod
    return m

def mod_factorial(mod, n):
    '''
    >>> mod_factorial(1000000007, 10)
    3628800
    >>> mod_factorial(7, 6)
    6
    '''
    return mod_permutation(mod, n, n)

def mod_combination(mod, n, r):
    '''
    >>> mod_combination(1000000007, 10, 2)
    45
    >>> mod_combination(7, 10, 2)
    3
    '''
    return mod_permutation(mod, n, r) * mod_inv(mod, mod_factorial(mod, r)) % mod

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
    
    def _mod_inv(self, n):
        return mod_inv(self._mod, n)
    
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


if __name__ == '__main__':
    #test()
    main()
