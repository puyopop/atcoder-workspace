#!/usr/bin/env python3
import sys

def solve(N: int, A: "List[int]"):
    from math import gcd
    from functools import reduce
    from collections import Counter
    from itertools import chain
    pu = PrimeUtil(1_000_100)
    c = Counter(chain.from_iterable(map(pu.unique_factor_iter, A)))
    if max(c.values(), default=1) == 1:
        return "pairwise coprime"
    return "setwise coprime" if reduce(gcd, A) == 1 else "not coprime"

class PrimeUtil:

    def __init__(self, size):
        self.size = size
        self._init_table()
  
    def _init_table(self):
        from itertools import takewhile
        self._min_factor = list(range(self.size))
        for i in takewhile(lambda x: x*x<=self.size, range(2, self.size)):
            if self._min_factor[i] != i:
                continue
            for j in range(i+i, self.size, i):
                self._min_factor[j] = i if i < self._min_factor[j]  else self._min_factor[j]

    def is_prime(self, n):
        """
        >>> pu = PrimeUtil(45)
        >>> pu.is_prime(1)
        False
        >>> pu.is_prime(2)
        True
        >>> pu.is_prime(3)
        True
        >>> pu.is_prime(37)
        True
        """
        assert n > 0
        if n == 1:
            return False
        return self._min_factor[n] == n

    def prime_iter(self):
        return filter(lambda x: self._min_factor[x] == x, range(2, self.size))

    def primes(self):
        """
        >>> pu = PrimeUtil(45)
        >>> pu.primes()
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
        """
        return tuple(self.prime_iter())

    def factor_iter(self, n):
        m = n
        while m != 1:
            yield self._min_factor[m]
            m //= self._min_factor[m]
    
    def factors(self, n):
        """
        >>> pu = PrimeUtil(30)
        >>> pu.factors(6)
        (2, 3)
        >>> pu.factors(12)
        (2, 2, 3)
        >>> pu.factors(24)
        (2, 2, 2, 3)
        >>> pu.factors(15)
        (3, 5)
        """
        return tuple(self.factor_iter(n))

    def unique_factor_iter(self, n):
        m = n
        while m != 1:
            # p := self._min_factor[m]
            p = self._min_factor[m]            
            yield p
            while m % p == 0:
                m //= p
    
    def unique_factors(self, n):
        """
        >>> pu = PrimeUtil(30)
        >>> pu.unique_factors(6)
        (2, 3)
        >>> pu.unique_factors(12)
        (2, 3)
        >>> pu.unique_factors(24)
        (2, 3)
        >>> pu.unique_factors(15)
        (3, 5)
        """
        return tuple(self.unique_factor_iter(n))

def test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test()
