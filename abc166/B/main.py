#!/usr/bin/env python3


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    N, K = list(map(int, input().split()))
    A = []
    for _ in range(K):
        _ = input()
        A.append(list(map(int, input().split())))
    B = set()
    for a in A:
        for aa in a:
            B.add(aa)
    print(N - len(B))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
