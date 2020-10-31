class PrimeUtil:

    def __init__(self, size):
        self.size = size
        self._init_table()
  
    def _init_table(self):
        from itertools import takewhile
        self._minimum_factor = list(range(self.size))
        self._is_prime = [True] * self.size
        self._is_prime[0] = False
        self._is_prime[1] = False
        for i in takewhile(lambda x: x*x<=self.size, range(self.size)):
            if not self._is_prime[i]:
                continue
            for j in range(i+i, self.size, i):
                self._is_prime[j] = False

    def prime_iter(self):
        return filter(lambda x: self._is_prime[x], range(self.size))

    def primes(self):
        """
        >>> pu = PrimeUtil(45)
        >>> pu.primes()
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
        """
        return tuple(self.prime_iter())

    def factor_iter(self, n):
        """
        >>> pu = PrimeUtil(30)
        >>> tuple(pu.factor_iter(6))
        (2, 3)
        >>> tuple(pu.factor_iter(12))
        (2, 2, 3)
        >>> tuple(pu.factor_iter(24))
        (2, 2, 2, 3)
        >>> tuple(pu.factor_iter(15))
        (3, 5)
        """
        from itertools import takewhile
        m = n
        for p in self.prime_iter():
            while m % p == 0:
                yield p
                m //= p
            if m == 1:
                return
    
    def factors(self, n):
        return tuple(self.factor_iter(n))

def test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test()
