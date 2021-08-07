"""
<Implementation>
<BFS>
"""
from sys import *
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# INPUT
N = int(stdin.readline().rstrip())
SPACE = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

SIZE = 2 # shart size
EAT = 0 # eat fishes
TIME = 0 # time

# <BFS> START
def bfs(i, j):
    global SIZE, EAT

    QUEUE = deque() # queue
    VISIT = [[False] * N for _ in range(N)] # visit
    FISH = [] # available fish

    # start
    QUEUE.append((i, j, 0)) 
    VISIT[i][j] = True

    while QUEUE:
        x, y, dist = QUEUE.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not VISIT[nx][ny]:
                if 0 < SPACE[nx][ny] < SIZE:
                    # able to eat
                    FISH.append((dist + 1, nx, ny))
                if SPACE[nx][ny] <= SIZE:
                    #able to move
                    QUEUE.append((nx, ny, dist + 1))
                    VISIT[nx][ny] = True

    if not FISH:
        # any fish available
        return -1, -1, -1

    EAT += 1
    if EAT >= SIZE:
        SIZE += 1
        EAT = 0
    FISH.sort(key=lambda x: (x[0], x[1], x[2])) # sort fish
    return FISH[0][0], FISH[0][1], FISH[0][2]
# <BFS> END

for i in range(N):
    for j in range(N):
        if SPACE[i][j] == 9:
            # find shark's start point
            POS = [i, j]
            SPACE[i][j] = 0
            break

while True:
    # call BFS
    time, POS[0], POS[1] = bfs(POS[0], POS[1])
    if POS[0] == -1 and POS[1] == -1:
        break
    
    SPACE[POS[0]][POS[1]] = 0
    TIME += time

print(TIME)