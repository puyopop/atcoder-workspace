#!/usr/bin/env python3
import sys


def solve(H: int, W: int, S: "List[str]"):
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
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    print(solve(H, W, S))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
