#!/usr/bin/env python3
import sys



def solve(N: int):
    from itertools import product, count, takewhile
    ans = 0
    for i in range(10):
        for s in product('357', repeat=i):
            if any(c not in s for c in '357'):
                continue
            if int(''.join(s)) <= N:
                ans += 1
    return ans


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    print(solve(N))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
