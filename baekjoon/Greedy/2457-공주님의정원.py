"""
<Greedy>
"""
from sys import *
from datetime import date

# DATE DIFFERENCE -> NUMBER
def dayToNum(flower):
    start = date(2021, flower[0], flower[1]) - date(2021, 1, 1)
    end = date(2021, flower[2], flower[3]) - date(2021, 1, 1)
    return [start.days + 1, end.days + 1]


# INPUT
N = int(stdin.readline().rstrip())
FLOWER = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

START = (date(2021, 3, 1) - date(2021, 1, 1)).days + 1  # 60
END = (date(2021, 11, 30) - date(2021, 1, 1)).days + 1  # 334

# SET DATE
DATE = []
for flower in FLOWER:
    DATE.append(dayToNum(flower))
DATE.sort()

# INIT VARIABLE
idx = -1  # index
temp = 0  # temp date
answer = 0  # output
poss = True  # deal with exception

while True:
    # END CONDITION
    if idx >= N or START > END:
        break

    # EXCEPTION FLAG
    flag = False

    # next index
    idx += 1

    # index ~ N
    for i in range(idx, N):
        # STOP CONDITION
        if START < DATE[i][0]:
            break

        # AVAILABLE CONDITION
        if temp < DATE[i][1]:
            # UPDATE
            temp = DATE[i][1]
            idx = i
            flag = True

    if flag:
        answer += 1
        START = temp
    else:
        poss = False
        break

if poss:
    print(answer)
else:
    print(0)