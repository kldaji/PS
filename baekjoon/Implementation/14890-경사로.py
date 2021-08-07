"""
<Implementation>
"""
from sys import *

# INPUT
N, L = map(int, stdin.readline().rstrip().split())
MAP = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]


def check(road):
    slope = [False] * N
    for i in range(N - 1):
        if road[i] == road[i + 1]:
            continue
        if road[i] - road[i + 1] == -1:
            # UP
            if not slope[i]:
                slope[i] = True
                if i - L + 1 >= 0:
                    for k in range(i - L + 1, i):
                        if road[k] - road[i + 1] != -1 or slope[k]:
                            return False
                        slope[k] = True
                else:
                    # out of range
                    return False
            else:
                # slope
                return False
        elif road[i] - road[i + 1] == 1:
            # DOWN
            if not slope[i + 1]:
                slope[i + 1] = True
                if i + L < N:
                    for k in range(i + 2, i + L + 1):
                        if road[i] - road[k] != 1 or slope[k]:
                            return False
                        slope[k] = True
                else:
                    # out of range
                    return False
            else:
                # slope
                return False
        else:
            # difference >= 2
            return False

    return True


ANSWER = 0

# CHECK ROW
for row in MAP:
    if check(row):
        ANSWER += 1

# CHECK COLUMN
for j in range(N):
    col = []
    for i in range(N):
        col.append(MAP[i][j])

    if check(col):
        ANSWER += 1

# OUTPUT
print(ANSWER)