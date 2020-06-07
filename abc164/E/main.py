#!/usr/bin/env python3
import sys

def solve(N: int, M: int, S: int, U: "List[int]", V: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    from collections import namedtuple
    from heapq import heappush, heappop
    MAX_COIN = sum(A)
    State = namedtuple('State', 'cost city coin')
    Edge = namedtuple('Edge', 'to fee cost')
    edges = [[] for _ in range(N+1)]
    for u, v, a, b in zip(U, V, A, B):
        edges[u].append(Edge(v, a, b))
        edges[v].append(Edge(u, a, b))
    for i, (c, d) in enumerate(zip(C, D), 1):
        edges[i].append(Edge(i, -c, d))
    hq = [State(0, 1, min(S, MAX_COIN))]
    min_costs = [[None] * (MAX_COIN+1) for _ in range(N+1)]
    while hq:
        s = heappop(hq)
        if min_costs[s.city][s.coin]:
            continue
        min_costs[s.city][s.coin] = s.cost
        for edge in edges[s.city]:
            if edge.fee > s.coin:
                continue
            ns = State(s.cost+edge.cost, edge.to, s.coin-edge.fee)
            if ns.coin > MAX_COIN or min_costs[ns.city][ns.coin]:
                continue
            heappush(hq, ns)
    return [min(filter(lambda x:x, c)) for c in min_costs[2:]]
        

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    print(*solve(N, M, S, U, V, A, B, C, D), sep='\n')

if __name__ == '__main__':
    main()
