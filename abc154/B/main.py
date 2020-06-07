#!/usr/bin/env python3
import sys


def solve(S: str):
    return 'x' * len(S)

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    print(solve(S))

if __name__ == '__main__':
    main()
