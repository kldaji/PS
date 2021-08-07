"""
<DFS>
"""
from sys import *

setrecursionlimit(10 ** 6)

def dfs(curr):
    # visit check
    visited[curr] = True

    # traversal connected node
    for node in graph[curr]:
        if not visited[node]:
            dfs(node)


# N : node (1 ~ 1000)
# M : edge (1 ~ N(N-1)/2)
N, M = map(int, stdin.readline().rstrip().split())

# Graph (node starts with 1 not 0)
graph = [[] for _ in range(N + 1)]

# visited
visited = [False] * (N + 1)

# number of edges
for _ in range(M):
    # u -> v
    # v -> u
    u, v = map(int, stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

connected = 0

# traversal(1 ~ N)
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        connected += 1

print(connected)
