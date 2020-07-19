from collections import namedtuple, defaultdict
from heapq import heappush, heappop
State = namedtuple('State', 'cost node')
Edge = namedtuple('Edge', 'to cost')

def dijkstra(start, end, edges):
    hq = [start]
    visited = set()
    while hq:
        s = heappop(hq)
        if s.node in visited:
            continue
        if s.node == end:
            return s.cost
        visited.add(s.node)
        for n, c in edges[s.node]:
            if n in visited:
                continue
            heappush(hq, State(s.cost+c, n))
    return -1
