"""
<DFS>
"""
from sys import *

setrecursionlimit(10 ** 6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, color):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # in range & not visited & same color
        if (
            0 <= nx < N
            and 0 <= ny < N
            and not visited[nx][ny]
            and colors[nx][ny] == color
        ):
            dfs(nx, ny, color)


def dfs_color_blind(x, y, color):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # in range & not visited
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # R or G & G or R & same color
            if (
                color == "R"
                and colors[nx][ny] == "G"
                or color == "G"
                and colors[nx][ny] == "R"
                or color == colors[nx][ny]
            ):
                dfs_color_blind(nx, ny, color)


# N : (1 ~ 100)
N = int(stdin.readline().rstrip())

colors = []
visited = [[False] * N for _ in range(N)]

# get color info
for _ in range(N):
    colors.append(list(stdin.readline().rstrip()))

# answer
answer = [0, 0]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, colors[i][j])
            answer[0] += 1

# init visited
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs_color_blind(i, j, colors[i][j])
            answer[1] += 1

# print with white space
print(" ".join(map(str, answer)))