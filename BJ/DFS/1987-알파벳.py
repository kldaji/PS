"""
<DFS>
<BackTracking>
"""

"""
<오답>
"""
from sys import *

setrecursionlimit(10 ** 6)

# move
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, cnt):
    global answer, alphas

    answer = max(answer, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in alphas:
            alphas.append(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            alphas.remove(board[nx][ny])


# R : height (1 ~ 20)
# C : width (1 ~ 20)
R, C = map(int, stdin.readline().rstrip().split())

# Board
board = []

for _ in range(R):
    board.append(list(stdin.readline().rstrip()))

# answer
answer = 0

alphas = [board[0][0]]

# x, y, cnt
dfs(0, 0, 1)

print(answer)
