#!/usr/bin/env python3
import sys


def solve(H: "List[int]"):
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    print(solve(H))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
