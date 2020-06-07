#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[str]"):
    a = tuple(map(set, a))
    ans = []
    for b, c in zip(a, reversed(a)):
        d = b & c
        if not d:
            return -1
        ans.append(next(iter(d)))
    return ''.join(ans)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [next(tokens) for _ in range(N)]  # type: "List[str]"
    print(solve(N, a))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
