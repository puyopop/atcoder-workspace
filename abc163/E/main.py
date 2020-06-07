#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    from collections import defaultdict
    dp = defaultdict(int)
    B = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
    for step, (i, a) in enumerate(B, 1):
        #print('i={}, a={}'.format(i, a))
        for left in range(step):
            right = N - step + left
            #print('[{},{}]'.format(left, right))
            #print('left[{},{}]: {} vs {}+{}'.format(left+1, right, dp[(left+1, right)], dp[(left, right)], abs(left-i)*a))
            #print('right[{},{}]: {} vs {}+{}'.format(left, right-1, dp[(left+1, right)], dp[(left, right)],abs(right-i)*a))
            dp[(left+1, right)] = max(dp[(left+1, right)], dp[(left, right)] + abs(left-i)*a)
            dp[(left, right-1)] = max(dp[(left, right-1)], dp[(left, right)] + abs(right-i)*a)    
    return max(v for v in dp.values())


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, A))

if __name__ == '__main__':
    main()
