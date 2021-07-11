"""
<Implementation>
<BFS>
"""
from sys import *
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# INPUT
N, L, R = map(int, stdin.readline().rstrip().split())
WORLD = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

# <BFS> START
def bfs(a, b):
    QUEUE = deque()  # queue
    OPEN = [(a, b)]  # open
    total = WORLD[a][b]  # total

    # start
    QUEUE.append((a, b))
    VISIT[a][b] = True

    while QUEUE:
        x, y = QUEUE.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # open condition
            if 0 <= nx < N and 0 <= ny < N and not VISIT[nx][ny]:
                if L <= abs(WORLD[x][y] - WORLD[nx][ny]) <= R:
                    VISIT[nx][ny] = True
                    QUEUE.append((nx, ny))
                    OPEN.append((nx, ny))
                    total += WORLD[nx][ny]

    total //= len(OPEN)

    if len(OPEN) > 1:
        # update
        for x, y in OPEN:
            WORLD[x][y] = total

        # number of open country
        return len(OPEN)

    # open nothing
    return 0


# <BFS> END

MOVE = 0

while True:
    VISIT = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not VISIT[i][j]:
                cnt += bfs(i, j)

    if cnt == 0:
        break

    MOVE += 1

print(MOVE)
