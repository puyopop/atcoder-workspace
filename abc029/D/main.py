#!/usr/bin/env python3
import sys

def solve_slow(N):
    return sum(n.count('1') for n in map(str, range(N+1)))

def solve(N: int):
    def f(n, m, b):
        if n == 0:
            return
        yield n // 10 * b
        if n % 10 == 1:
            yield m + 1
        if n % 10 > 1:
            yield b
        yield from f(n//10, (n % 10) * b + m, b * 10)
    return sum(f(N, 0, 1))

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    # print(solve_slow(N))
    print(solve(N))

if __name__ == '__main__':
    main()
