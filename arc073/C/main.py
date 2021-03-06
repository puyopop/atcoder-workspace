#!/usr/bin/env python3
import sys


def solve(N: int, T: int, t: "List[int]"):
    a = [[t[0]]]
    for tt in t[1:]:
        if a[-1][-1] + T < tt:
            a.append([tt])
        else:
            a[-1].append(tt)
    b = [aa[-1] - aa[0] + T for aa in a]    
    return sum(b)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    t = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, T, t))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
