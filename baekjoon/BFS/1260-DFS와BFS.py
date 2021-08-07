from sys import *

N, M, V = map(int, stdin.readline().rstrip().split())

# 2차원 배열 (N X N)
graph = [[] for _ in range(N + 1)]

# 0 ~ N
visit = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [V]

for i in range(N + 1):
    graph[i].sort(reverse=True)

while stack:
    curr = stack.pop()

    if not visit[curr]:
        print(curr, end=" ")
    else:
        continue

    visit[curr] = True

    for node in graph[curr]:
        if not visit[node]:
            stack.append(node)

print()

queue = []
visit = [False for _ in range(N + 1)]

for i in range(N + 1):
    graph[i].sort()

queue.append(V)

while queue:
    curr = queue.pop(0)

    if not visit[curr]:
        print(curr, end=" ")
    else:
        continue

    visit[curr] = True

    for node in graph[curr]:
        if not visit[node]:
            queue.append(node)
