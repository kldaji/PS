"""
<BFS>
"""

from sys import *
from collections import deque

# move
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# M : width (2 ~ 1,000)
# N : height (2 ~ 1,000)
M, N = map(int, stdin.readline().rstrip().split())

tomatos = []

for _ in range(N):
    tomato = list(map(int, stdin.readline().rstrip().split()))
    tomatos.append(tomato)

queue = deque()

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            # append tomato
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                queue.append((nx, ny))

done = True

answer = -2

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 0:
            done = False

        answer = max(answer, tomatos[i][j])

if not done:
    print(-1)
else:
    if answer == -1:
        print(0)
    else:
        print(answer - 1)
