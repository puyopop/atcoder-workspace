#!/usr/bin/env python3
import sys


def solve(T: "List[int]", A: "List[int]", B: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    A = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    print(solve(T, A, B))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
