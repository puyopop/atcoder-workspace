#!/usr/bin/env python3
import sys
from collections import namedtuple, defaultdict
from heapq import heappush, heappop, heapify
State = namedtuple('State', 'cost node, pre')
Edge = namedtuple('Edge', 'to cost')

MOD = 1000000007  # type: int

def dijkstra(init_states, end, edges):
    hq = init_states    
    heapify(hq)
    min_costs = {}
    counts = defaultdict(int)
    counts[0] = 1
    while hq:
        #print("="*10)
        #print(min_costs)
        #print(counts)
        #print(hq)
        s = heappop(hq)
        if s.node in min_costs:
            if s.cost == min_costs[s.node]:
                counts[s.node] += counts[s.pre]
            continue
        if s.cost > min_costs.get(end, float('inf')):
            return counts[end]
        min_costs[s.node] = s.cost
        counts[s.node] += counts[s.pre]
        for n, c in edges[s.node]:
            if n in min_costs:
                continue
            heappush(hq, State(s.cost+c, n, s.node))
    return counts[end] % MOD

def solve(N: int, a: int, b: int, M: int, x: "List[int]", y: "List[int]"):
    edges = [[] for _ in range(N+1)]
    for xx, yy in zip(x, y):
        edges[xx].append(Edge(yy, 1))
        edges[yy].append(Edge(xx, 1))        
    return dijkstra([State(0, a, 0)], b, edges)


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    print(solve(N, a, b, M, x, y))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()
