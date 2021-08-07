from sys import *

# node 개수
N = int(stdin.readline().rstrip())

# edge 개수
edge = int(stdin.readline().rstrip())

# N X N
graph = [[] for _ in range(N + 1)]

for _ in range(edge):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 0 ~ N
visited = [False for _ in range(N + 1)]

# start with 1
queue = [1]
visited[1] = True

infected = 0

while queue:
    curr = queue.pop(0)

    for node in graph[curr]:
        if not visited[node]:
            infected += 1
            visited[node] = True
            queue.append(node)

print(infected)