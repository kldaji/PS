"""
<Brute Force>
"""
from sys import *
from copy import deepcopy

# RIGHt : 0
# DOWN : 1
# LEFT : 2
# UP : 3
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# N : height (1 ~ 8)
# M : width (1 ~ 8)
N, M = map(int, stdin.readline().rstrip().split())

# one : 0 | 1 | 2 | 3
# two : (0,2) | (1,3)
# three : (0,1) | (1,2) | (2,3) | (3,0)
# four : (0,1,2) | (1,2,3) | (0,2,3) | (0,3,1)
# five : (0,1,2,3)
DIRECTION = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 3, 1]],
    [[0, 1, 2, 3]],
]


def fill(x, y, temp, dir):
    for d in dir:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]

            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = "#"
            else:
                break


def dfs(room, cnt):
    global ANSWER

    # store temporary
    temp = deepcopy(room)

    if cnt == len(CCTV):
        BLIND = 0

        for i in range(N):
            BLIND += room[i].count(0)

        ANSWER = min(ANSWER, BLIND)
        return

    x, y, num = CCTV[cnt]

    for dir in DIRECTION[num]:
        fill(x, y, temp, dir)
        # next cctv
        dfs(temp, cnt + 1)
        # restore
        temp = deepcopy(room)


ROOM = []
for _ in range(N):
    ROOM.append(list(map(int, stdin.readline().rstrip().split())))

CCTV = []
ANSWER = maxsize

for i in range(N):
    for j in range(M):
        if 1 <= ROOM[i][j] <= 5:
            # x, y, cctv_num
            CCTV.append([i, j, ROOM[i][j]])

# start
dfs(ROOM, 0)

print(ANSWER)
