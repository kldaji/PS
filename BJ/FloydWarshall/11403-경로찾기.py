"""
<FloydWarshall>
- 모든 정점에서 모든 정점으로의 최단거리를 구하는 알고리즘
- 거쳐가는 정점을 기준으로 최단거리를 구한다???
"""

from sys import *

# number of nodes (1 ~ 100)
N = int(stdin.readline().rstrip())

# Graph
graph = []

for _ in range(N):
    graph.append(list(stdin.readline().rstrip().split()))

# check all nodes
for i in range(N):
    for j in range(N):
        for k in range(N):
            # i : pass node
            if graph[j][k] == "0" and graph[j][i] == "1" and graph[i][k] == "1":
                graph[j][k] = "1"

for g in graph:
    print(" ".join(g))
