"""
<Brute Force>
"""
from sys import *

"""
<Example>
5457
3
6 7 8

5455 -> 5456 -> 5457

500000
8
0 2 3 4 6 7 8 9
511111 -> 500000
"""

# N : (0 ~ 500,000)
N = int(stdin.readline().rstrip())

# M : (0 ~ 9)
M = int(stdin.readline().rstrip())

BROKEN = set(map(int, stdin.readline().rstrip().split()))


def possible(CHANNEL):
    for i in range(len(CHANNEL)):
        if int(CHANNEL[i]) in BROKEN:
            return False
    return True


# init (100 -> N)
ANSWER = abs(N - 100)

for i in range(500001 * 2):
    # able to click
    if possible(str(i)):
        # button click + (++ or --) click
        temp = len(str(i)) + abs(N - i)
        ANSWER = min(ANSWER, temp)

print(ANSWER)