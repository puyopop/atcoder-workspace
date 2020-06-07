#!/usr/bin/env python3


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    from collections import Counter
    from itertools import chain
    N, M = list(map(int, input().split()))
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    c = Counter(chain(*A))
    print(len([v for v in c.values() if v >= N]))
    

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
