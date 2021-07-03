"""
<Brute Force>
"""
from sys import *

# N : cities (2 ~ 10)
N = int(stdin.readline().rstrip())


def dfs(city, cnt, expense, start):
    global ANSWER

    if cnt == N:
        # except no way
        if GRAPH[city][start] != 0:
            # add final destination
            expense += GRAPH[city][start]
            ANSWER = min(ANSWER, expense)
        return

    for i in range(N):
        # except own self & no way
        if i != city and not VISIT[i] and GRAPH[city][i] != 0:
            VISIT[i] = True
            dfs(i, cnt + 1, expense + GRAPH[city][i], start)
            VISIT[i] = False


GRAPH = []
VISIT = [False] * N
ANSWER = maxsize

for _ in range(N):
    GRAPH.append(list(map(int, stdin.readline().rstrip().split())))

# start point
for i in range(N):
    VISIT[i] = True
    # start city, cnt, expense, start city
    dfs(i, 1, 0, i)
    VISIT[i] = False
print(ANSWER)