#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(H: int, W: int, a: "List[List[str]]"):
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    a = [[next(tokens) for _ in range(1)] for _ in range(H)]  # type: "List[List[str]]"
    print(solve(H, W, a))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()