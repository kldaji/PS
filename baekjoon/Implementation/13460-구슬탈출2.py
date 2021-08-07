"""
<Implementation>
<BFS>
"""
from sys import *
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# INPUT
N, M = map(int, stdin.readline().rstrip().split())
BOARD = [list(stdin.readline().rstrip()) for _ in range(N)]
VISIT = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]


def move(x, y, dx, dy):
    dd = 0
    while BOARD[x][y] != "O" and BOARD[x + dx][y + dy] != "#":
        x += dx
        y += dy
        dd += 1

    return x, y, dd


def bfs():
    QUEUE = deque()  # queue

    # Red, Blue
    for i in range(N):
        for j in range(M):
            if BOARD[i][j] == "R":
                rx, ry = i, j
            elif BOARD[i][j] == "B":
                bx, by = i, j

    # start
    QUEUE.append([rx, ry, bx, by, 1])
    VISIT[rx][ry][bx][by] = True

    # BFS
    while QUEUE:
        rx, ry, bx, by, d = QUEUE.popleft()

        if d > 10:
            return -1
        for i in range(4):
            nrx, nry, rd = move(rx, ry, dx[i], dy[i])
            nbx, nby, bd = move(bx, by, dx[i], dy[i])

            if BOARD[nbx][nby] != "O":
                if BOARD[nrx][nry] == "O":
                    return d

                if nrx == nbx and nry == nby:
                    if rd > bd:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not VISIT[nrx][nry][nbx][nby]:
                    VISIT[nrx][nry][nbx][nby] = True
                    QUEUE.append([nrx, nry, nbx, nby, d + 1])
    return -1


print(bfs())