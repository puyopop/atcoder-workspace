#!/usr/bin/env python3
import sys
import math

def solve(N, S, Q, queries):
    def update(i, c):
        cc = values[i]
        buckets[i//rN][cc] -= 1
        buckets[i//rN][c] += 1
        values[i] = c

    def count(l, r):
        print('---count---')
        res = [0] * (ord('z')-ord('a')+1)
        for i in range(rN):
            ll = i * rN
            rr = ll + rN
            print('l={}, r={}, ll={}, rr={}'.format(l, r, ll, rr))
            if r <= ll or rr <= l:
                print('--1')
                continue
            if l <= ll and rr <= r:
                print('--2')
                for i, v in enumerate(buckets[i]):
                    res[i] += v
            else:
                print('--3', max(l, ll), '->', min(r, rr))
                for i in range(max(l, ll), min(r, rr)):
                    print('values[{}]={}, values={}'.format(i, values[i], values))
                    res[values[i]] += 1
            print(res)
        return sum(n > 0 for n in res)
        
    rN = math.ceil(N ** 0.5)
    values = [ord(c)-ord('a') for c in S]
    buckets = [[0] * (ord('z')-ord('a')+1) for _ in range(rN)]
    for i, v in enumerate(values):
        buckets[i//rN][v] += 1
    for t, x, y in queries:
        if t == 1:
            update(int(x)-1, ord(y)-ord('a'))
        else:
            yield count(int(x)-1, int(y))
        #print(t, x, y)
        #print(*buckets, sep='\n')


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    S = next(tokens)
    Q = int(next(tokens))
    queries = [(int(next(tokens)), next(tokens), next(tokens)) for _ in range(Q)]
    for result in solve(N, S, Q, queries):
        print(result)

if __name__ == '__main__':
    main()
