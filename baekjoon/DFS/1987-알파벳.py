"""
<DFS>
<BackTracking>
"""
from sys import *

# move
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# alpha
ALPHA = [0] * 26


def dfs(x, y, cnt):
    global answer

    answer = max(answer, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and ALPHA[board[nx][ny]] == 0:
            ALPHA[board[nx][ny]] = 1
            dfs(nx, ny, cnt + 1)
            ALPHA[board[nx][ny]] = 0


# R : height (1 ~ 20)
# C : width (1 ~ 20)
R, C = map(int, stdin.readline().rstrip().split())

# Board
board = []

for _ in range(R):
    board.append(list(map(lambda x: ord(x) - 65, stdin.readline().rstrip())))

# answer
answer = 1

# init
ALPHA[board[0][0]] = 1

# x, y, cnt
dfs(0, 0, answer)

print(answer)
