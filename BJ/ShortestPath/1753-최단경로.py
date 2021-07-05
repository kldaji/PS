"""
<Dijkstra>
- 하나의 노드(기준점)에서 출발하여 다른 모든 노드까지의 최단 경로를 구하는 알고리즘.
"""
from sys import *
import heapq

# Define INF which is big enough
INF = int(10e9)

# 정점의 개수 V (1 ~ 20,000), 간선의 개수 E (1 ~ 300,000)
V, E = map(int, stdin.readline().rstrip().split())

# 시작 정점
K = int(stdin.readline().rstrip())

# Graph
graph = [[] for _ in range(V + 1)]

# distance
dist = [INF] * (V + 1)

# E개의 간선
for _ in range(E):
    # u -> v (w)
    u, v, w = map(int, stdin.readline().rstrip().split())

    # u -> (w,v)
    graph[u].append((w, v))

# Setting for start node
dist[K] = 0

# priority queue
heap = [(0, K)]

# Loop until heap is empty
while heap:
    # current node
    cw, curr = heapq.heappop(heap)

    # check connection
    for weight, node in graph[curr]:
        # update condition
        if dist[node] > (dist[curr] + weight):
            dist[node] = dist[curr] + weight
            heapq.heappush(heap, (dist[node], node))

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])