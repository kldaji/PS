"""
<Greedy>
"""
from sys import *

# N (1 ~ 50)
N = int(stdin.readline().rstrip())

WEIGHT_LIMIT = list(map(int, stdin.readline().rstrip().split()))
WEIGHT_LIMIT.sort(reverse=True)

# M (1 ~ 10,000)
M = int(stdin.readline().rstrip())

BOX_WEIGHT = list(map(int, stdin.readline().rstrip().split()))
BOX_WEIGHT.sort(reverse=True)


if BOX_WEIGHT[0] > WEIGHT_LIMIT[0]:
    # not able to move
    print(-1)
else:
    MINUTE = 0

    while BOX_WEIGHT:
        MINUTE += 1
        for crane in WEIGHT_LIMIT:
            for box in BOX_WEIGHT:
                if crane >= box:
                    BOX_WEIGHT.remove(box)
                    break
    print(MINUTE)
