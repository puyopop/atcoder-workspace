#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    from functools import reduce
    xyz_list = [[0]*3]
    for a in A:        
        xyz_list.append(xyz_list[-1][:])
        xyz_list[-1][xyz_list[-1].index(a)] += 1
    T = [xyz.count(a) for xyz, a in zip(xyz_list, A)]
    return reduce(lambda a,b: a*b%MOD, T)

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
