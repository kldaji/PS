"""
<Greedy>
"""
from sys import *

"""
<Example>
-37 2 -6 -39 -29 11 -28

-39 -37 -29 -28 -6
11 2

39 + 29*2 + 6*2
11*2
"""

# N (1 ~ 10,000)
# M (1 ~ 10,000)
N, M = map(int, stdin.readline().rstrip().split())

BOOK = list(map(int, stdin.readline().rstrip().split()))

ANSWER = 0

NEG = []
POS = []

for book in BOOK:
    if book < 0:
        NEG.append(book)
    elif book > 0:
        POS.append(book)

# ascending
NEG.sort()

# descending
POS.sort(reverse=True)

if not NEG:
    # only positive
    for i in range(M, len(POS), M):
        ANSWER += POS[i] * 2

    # one way
    ANSWER += POS[0]
elif not POS:
    # only negative
    for i in range(M, len(NEG), M):
        ANSWER += abs(NEG[i]) * 2

    # one way
    ANSWER += abs(NEG[0])
else:
    # both
    if POS[0] > abs(NEG[0]):
        # one way
        ANSWER += POS[0]
        for i in range(M, len(POS), M):
            ANSWER += POS[i] * 2
        for i in range(0, len(NEG), M):
            ANSWER += abs(NEG[i]) * 2
    else:
        # one way
        ANSWER += abs(NEG[0])
        for i in range(0, len(POS), M):
            ANSWER += POS[i] * 2
        for i in range(M, len(NEG), M):
            ANSWER += abs(NEG[i]) * 2

print(ANSWER)