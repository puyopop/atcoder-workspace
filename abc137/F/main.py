#!/usr/bin/env python3
import sys

MOD = 2  # type: int


def solve(p: int, a: "List[int]"):
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    p = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(p - 1 - 0 + 1)]  # type: "List[int]"
    solve(p, a)

if __name__ == '__main__':
    main()
