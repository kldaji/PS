"""
<Bit Masking>
<BFS>
"""

from sys import *

# W(0), N(1), E(2), S(3)
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
# North : (0,-1)
# South : (0,1)

# n : width (1 ~ 50)
# m : height (1 ~ 50)
n, m = map(int, stdin.readline().rstrip().split())

# input list
castles = []
visited = [[False] * n for _ in range(m)]


# get bit
def getBit(i, j, idx):
    ret = (castles[i][j] & (1 << idx)) != 0
    return ret


# 0 -> 1, 1 -> 0
def toggleBit(i, j, idx):
    castles[i][j] = castles[i][j] ^ (1 << idx)


# bfs
def bfs(i, j):
    queue = [(i, j)]
    visited[i][j] = True

    cnt = 0

    while queue:
        x, y = queue.pop(0)
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not getBit(x, y, i) and not visited[nx][ny]:
                    # bit is 0 & not visited yet
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return cnt


# get input
for _ in range(m):
    castles.append(list(map(int, stdin.readline().rstrip().split())))

# answer list
answer = [0, 0, 0]

# bfs
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            answer[1] = max(bfs(i, j), answer[1])
            answer[0] += 1

# remove one wall
for i in range(m):
    for j in range(n):
        for k in range(4):
            if getBit(i, j, k):
                # init visited list
                visited = [[False] * n for _ in range(m)]
                # 1 -> 0
                toggleBit(i, j, k)
                # bfs
                answer[2] = max(bfs(i, j), answer[2])
                # 0 -> 1
                toggleBit(i, j, k)

for ans in answer:
    print(ans)