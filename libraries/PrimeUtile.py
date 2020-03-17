class PrimeUtil:

    def __init__(self, size):
        self.size = size
        self._init_table()
  
    def _init_table(self):
        from itertools import takewhile
        self._is_prime = [True] * self.size
        self._is_prime[0] = False
        self._is_prime[1] = False
        for i in takewhile(lambda x: x*x<=self.size, range(self.size)):
            if not self._is_prime[i]:
                continue
            print(i)
            for j in range(i+i, self.size, i):
                self._is_prime[j] = False

    def prime_iter(self):
        return filter(lambda x: self._is_prime[x], range(self.size))

    def primes(self):
        return tuple(self.prime_iter())

    def factor_iter(self, n):
        from itertools import takewhile
        print(n)
        m = n
        for p in self.prime_iter():
            while m % p == 0:
                yield p
                m //= p
            if m == 1:
                return
    
    def factors(self, n):
        return tuple(self.factor_iter(n))
