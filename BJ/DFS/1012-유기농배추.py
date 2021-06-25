"""
<DFS>
"""
from sys import *

setrecursionlimit(10 ** 6)

# move
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global visited, N, M, ground

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and ground[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


# test case
T = int(stdin.readline().rstrip())

for _ in range(T):
    # M : width (1 ~ 50)
    # N : height (1 ~ 50)
    # K : number of earthworms (1 ~ 2500)
    M, N, K = map(int, stdin.readline().rstrip().split())

    ground = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    earthworm = 0

    for _ in range(K):
        x, y = map(int, stdin.readline().rstrip().split())
        ground[y][x] = 1

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and ground[i][j] == 1:
                dfs(i, j)
                earthworm += 1

    print(earthworm)
