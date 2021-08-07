"""
<Greedy>
"""
from sys import *

# N (2 ~ 100,000)
N = int(stdin.readline().rstrip())


# first light on
def first_on(LIGHT):
    TURN = 1

    # 0 -> 1 | 1 -> 0
    LIGHT[0] ^= 1
    LIGHT[1] ^= 1

    for i in range(1, len(LIGHT)):
        if LIGHT[i - 1] == LIGHT_TARGET[i - 1]:
            continue

        # 0 -> 1 | 1 -> 0
        LIGHT[i - 1] ^= 1
        LIGHT[i] ^= 1

        if (i + 1) < len(LIGHT):
            # 0 -> 1 | 1 -> 0
            LIGHT[i + 1] ^= 1

        TURN += 1

    POSS = True

    for i in range(len(LIGHT)):
        if LIGHT[i] != LIGHT_TARGET[i]:
            POSS = False
            break
    if not POSS:
        return maxsize
    else:
        return TURN


def first_off(LIGHT):
    TURN = 0
    for i in range(1, len(LIGHT)):
        if LIGHT[i - 1] == LIGHT_TARGET[i - 1]:
            continue
        # 0 -> 1 | 1 -> 0
        LIGHT[i - 1] ^= 1
        LIGHT[i] ^= 1

        if (i + 1) < len(LIGHT):
            # 0 -> 1 | 1 -> 0
            LIGHT[i + 1] ^= 1

        TURN += 1

    POSS = True

    for i in range(len(LIGHT)):
        if LIGHT[i] != LIGHT_TARGET[i]:
            POSS = False
            break

    if not POSS:
        return maxsize
    else:
        return TURN


LIGHT_INIT = list(map(int, stdin.readline().rstrip()))
LIGHT_TARGET = list(map(int, stdin.readline().rstrip()))

ans = min(first_on(LIGHT_INIT[:]), first_off(LIGHT_INIT[:]))

if ans == maxsize:
    print(-1)
else:
    print(ans)