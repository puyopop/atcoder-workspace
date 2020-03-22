#!/usr/bin/env python3
import sys


def solve(n: int, a: "List[int]"):
    def _solve(op):
        from itertools import cycle
        ab = 0
        for aa in map(lambda a_o: a_o[0]*a_o[1], zip(a, cycle(op))):
            ab -= aa
            if ab >= 0:
                yield ab + 1
                ab = -1
            ab = abs(ab)
    return min(sum(_solve([1, -1])), sum(_solve([-1, 1])))

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    print(solve(n, a))

if __name__ == '__main__':
    main()
