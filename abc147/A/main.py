#!/usr/bin/env python3
import sys


def solve(A: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    print(solve(A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
