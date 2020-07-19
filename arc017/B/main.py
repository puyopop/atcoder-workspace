#!/usr/bin/env python3
import sys


def solve(N: int, K: int, A: "List[int]"):
    from itertools import islice
    ans, k = 0, 1
    for a0, a1 in zip(A, islice(A, 1, None)):
        ans += k >= K        
        if a0 >= a1:
            k = 0
        k += 1
    else:
        ans += k >= K
    return ans

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, K, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()