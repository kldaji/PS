"""
<DFS>
"""
from sys import *
setrecursionlimit(10 ** 6)

# move
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and MAP[nx][ny] == 1:
            # visited
            MAP[nx][ny] = -1
            dfs(nx, ny)


while True:
    # w : width (1 ~ 50)
    # h : height (1 ~ 50)
    w, h = map(int, stdin.readline().rstrip().split())

    # end condition
    if w == 0 and h == 0:
        break

    MAP = [list(map(int, stdin.readline().rstrip().split())) for _ in range(h)]

    ISLAND = 0

    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1:
                # visited
                MAP[i][j] = -1
                dfs(i, j)
                # island
                ISLAND += 1

    print(ISLAND)
