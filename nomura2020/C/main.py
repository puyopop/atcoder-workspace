#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    from itertools import islice
    cap = [1]
    for a in A:
        cap.append(2*(cap[-1]-a))
    ans = 0
    p = 0
    for a, c in zip(A[N::-1], cap[N::-1]):
        c -= a
        if 2 * c < p:
            return -1
        p = min(c, p) + a
        ans += p
    return ans

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 0 + 1)]  # type: "List[int]"
    print(solve(N, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
