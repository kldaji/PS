"""
<BFS>
"""
from sys import *
from collections import deque

N, K = map(int, stdin.readline().rstrip().split())

# pos, time
SUBIN = deque()
SUBIN.append((N, 0))

# visited
VISIT = [False] * 100001

# start
VISIT[N] = True

while SUBIN:
    pos, time = SUBIN.popleft()

    if pos == K:
        print(time)
        break

    if pos * 2 <= 100000 and not VISIT[pos * 2]:
        VISIT[pos * 2] = True
        SUBIN.append((pos * 2, time + 1))
    if pos + 1 <= 100000 and not VISIT[pos + 1]:
        VISIT[pos + 1] = True
        SUBIN.append((pos + 1, time + 1))
    if pos - 1 >= 0 and not VISIT[pos - 1]:
        VISIT[pos - 1] = True
        SUBIN.append((pos - 1, time + 1))
