from sys import *

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global apart, visited, N, answer

    visited[x][y] = True
    answer[-1] += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and apart[nx][ny] == 1:
            dfs(nx, ny)


N = int(stdin.readline().rstrip())

apart = []
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    apart.append(list(map(int, stdin.readline().rstrip())))

answer = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and apart[i][j] == 1:
            answer.append(0)
            dfs(i, j)

print(len(answer))

answer.sort()

for ans in answer:
    print(ans)
