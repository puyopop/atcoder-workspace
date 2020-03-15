#!/usr/bin/env python3
import sys
from itertools import count, islice

MOD = 1000000007  # type: int

def mod_factorial_iter():
    acc = 1
    yield 1
    for i in count(1):
        acc = acc * i % MOD
        yield acc

def solve(n: int, k: int):
    mod_factorials = tuple(islice(mod_factorial_iter(), n+2))
    def comb(a, b):
        return (mod_factorials[a] * (pow(mod_factorials[a-b], MOD-2, MOD) * pow(mod_factorials[b], MOD-2, MOD)) % MOD) % MOD
    ans = 1
    for i in range(1, min(n-1, k)+1):
        t = (comb(n-1, i) * comb(n, i)) % MOD
        ans = (ans + t) % MOD
    return ans


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    print(solve(n, k))

if __name__ == '__main__':
    main()
    
            
