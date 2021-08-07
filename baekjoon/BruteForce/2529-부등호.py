"""
<Brute Force>
<Back Tracking>
"""
from sys import *

MAX = 0
MIN = maxsize
ANSWER = [0, 0]

# INPUT
k = int(stdin.readline().rstrip())
INEQUAL = list(stdin.readline().rstrip().split())

# visit
VISIT = [False] * 10


def dfs(depth, LIST):
    global MAX, MIN, VISIT

    if depth == k:
        if MAX < int("".join(map(str, LIST))):
            ANSWER[0] = "".join(map(str, LIST))
            MAX = int("".join(map(str, LIST)))

        if MIN > int("".join(map(str, LIST))):
            ANSWER[1] = "".join(map(str, LIST))
            MIN = int("".join(map(str, LIST)))
        return

    for i in range(10):
        if not VISIT[i]:
            if (INEQUAL[depth] == ">" and LIST[-1] > i) or (
                INEQUAL[depth] == "<" and LIST[-1] < i
            ):
                LIST.append(i)
                VISIT[i] = True
                dfs(depth + 1, LIST)
                LIST.pop()
                VISIT[i] = False


for i in range(10):
    VISIT[i] = True
    dfs(0, [i])
    VISIT[i] = False

print(ANSWER[0])
print(ANSWER[1])