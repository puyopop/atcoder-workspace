#!/usr/bin/env python3

def main():
    from itertools import chain
    S = input()
    Q = int(input())
    Queries = [input().split() for _ in range(Q)]
    H_T = H, T = [], []
    flag = 0
    for query in Queries:
        if len(query) == 1:
            flag ^= 1
            continue
        _, f, c = query
        H_T[(int(f) + flag - 1) % 2].append(c)
    t = ''.join(chain(reversed(H), S, T))
    if flag:
        t = reversed(t)
    print(''.join(t))


if __name__ == '__main__':
    main()
