"""
<BFS>
"""
from sys import *
from collections import deque

# move
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# N : height (1 ~ 1000)
# M : width (1 ~ 1000)
N, M = map(int, stdin.readline().rstrip().split())

# map
MAP = []

for _ in range(N):
    MAP.append(list(stdin.readline().rstrip()))

# path
VISIT = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# x, y, wall
QUEUE = deque()
QUEUE.append([0, 0, 1])

# start
VISIT[0][0][1] = 1


def bfs():
    while QUEUE:
        x, y, w = QUEUE.popleft()

        if x == N - 1 and y == M - 1:
            return VISIT[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if MAP[nx][ny] == "1" and w == 1:
                    # wall
                    VISIT[nx][ny][0] = VISIT[x][y][1] + 1
                    QUEUE.append([nx, ny, 0])
                elif MAP[nx][ny] == "0" and VISIT[nx][ny][w] == 0:
                    # able to go
                    # not visited
                    VISIT[nx][ny][w] = VISIT[x][y][w] + 1
                    QUEUE.append([nx, ny, w])

    return -1


print(bfs())

"""
<INCORRECT>

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(queue, COPYMAP):
    global N, M

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and COPYMAP[nx][ny] == "0":
                COPYMAP[nx][ny] = COPYMAP[x][y] + 1
                queue.append((nx, ny))

    # not able to finish
    if COPYMAP[N - 1][M - 1] == "0":
        return -1
    else:
        return COPYMAP[N - 1][M - 1]


# N : height (1 ~ 1000)
# M : width (1 ~ 1000)
N, M = map(int, stdin.readline().rstrip().split())

# map
MAP = []

for _ in range(N):
    MAP.append(list(stdin.readline().rstrip()))

# start point
MAP[0][0] = 1

# walls
WALLS = []

for i in range(N):
    for j in range(M):
        if MAP[i][j] == "1":
            WALLS.append((i, j))

# answer
answer = maxsize

for wx, wy in WALLS:
    COPYMAP = MAP
    COPYMAP[wx][wy] = "0"

    # queue
    queue = deque()

    # start point
    queue.append((0, 0))

    # shortest path
    path = bfs(queue, COPYMAP)
    if path != -1:
        answer = min(path, answer)

    # recover
    COPYMAP[wx][wy] = "1"

if answer == maxsize:
    print(-1)
else:
    print(answer)
"""