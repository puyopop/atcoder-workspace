#!/usr/bin/env python3

def solve(N, A):
    from collections import defaultdict
    B = defaultdict(int)
    ans = 0
    for i, a in enumerate(A, 1):
        ans += B[a-i]
        B[-a-i] += 1
    return ans

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()