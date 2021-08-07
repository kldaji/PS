"""
<Dijkstra>
"""
from sys import *
import heapq

# INF
INF = int(10e9)

# number of cities (1 ~ 1000)
N = int(stdin.readline().rstrip())

# number of buses (1 ~ 100,000)
M = int(stdin.readline().rstrip())

# Graph (N x N)
graph = [[] for _ in range(N + 1)]

# bus route
for _ in range(M):
    # start, end, charge
    s, e, c = map(int, stdin.readline().rstrip().split())
    # start -> (charge, end)
    graph[s].append((c, e))

# start point, destination point
start, dest = map(int, stdin.readline().rstrip().split())

charge = [INF] * (N + 1)
heap = []

# Set start point
charge[start] = 0
heapq.heappush(heap, (0, start))

while heap:
    # current charge & node
    cc, curr = heapq.heappop(heap)

    if charge[curr] < cc:
        continue

    # next charge & node candidate
    for nc, next in graph[curr]:
        # total charge
        tc = cc + nc
        if charge[next] > tc:
            charge[next] = tc
            heapq.heappush(heap, (tc, next))

print(charge[dest])