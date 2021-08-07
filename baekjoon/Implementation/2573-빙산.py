"""
<Implementation>
<BFS>
"""
from sys import *
import copy
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# INPUT
N, M = map(int, stdin.readline().rstrip().split())
MAP = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

YEAR = 1

# <BFS> START
def bfs(i, j):
    global VISIT

    QUEUE = deque()
    QUEUE.append((i, j))

    while QUEUE:
        x, y = QUEUE.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not VISIT[nx][ny] and MAP[nx][ny] > 0:
                VISIT[nx][ny] = True
                QUEUE.append((nx, ny))


# <BFS> END

while True:
    VISIT = [[False] * M for _ in range(N)]
    MAP_COPY = copy.deepcopy(MAP)

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if MAP_COPY[ni][nj] == 0:
                    MAP[i][j] -= 1
            if MAP[i][j] < 0:
                MAP[i][j] = 0

    ICE = 0

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if not VISIT[i][j] and MAP[i][j] > 0:
                VISIT[i][j] = True
                bfs(i, j)
                ICE += 1

    # END CONDITION
    if ICE > 1:
        print(YEAR)
        break

    if ICE == 0:
        print(0)
        break

    YEAR += 1
