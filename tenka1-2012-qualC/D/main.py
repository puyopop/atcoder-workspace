#!/usr/bin/env python3
import sys


def solve(H: int, W: int, c: "List[str]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    c = [next(tokens) for _ in range(H - 1 - 0 + 1)]  # type: "List[str]"
    print(solve(H, W, c))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
