#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(N: int, p: "List[int]"):
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)

if __name__ == '__main__':
    main()
