"""
<Brute Force>
"""

from itertools import permutations
from sys import *

"""
N = int(stdin.readline().rstrip())

# number list
NUMBER = list(map(int, stdin.readline().rstrip().split()))

# answer
ANSWER = 0

PER = permutations(NUMBER)

for per in PER:
    total = 0
    for i in range(len(per) - 1):
        total += abs(per[i] - per[i + 1])

    ANSWER = max(ANSWER, total)

print(ANSWER)
"""

"""
<INCORRECT> - There would be same elements in NUMBER
<SOLUTION> - check index visited or not
"""


def permutation(LIST, NUMBER):
    global N, ANSWER
    if len(LIST) == N:
        total = 0
        for i in range(len(LIST) - 1):
            total += abs(LIST[i] - LIST[i + 1])

        ANSWER = max(ANSWER, total)
        return

    for i in range(N):
        if not visited[i]:
            LIST.append(NUMBER[i])
            visited[i] = True
            permutation(LIST, NUMBER)
            LIST.pop()
            visited[i] = False


N = int(stdin.readline().rstrip())

# number list
NUMBER = list(map(int, stdin.readline().rstrip().split()))

# answer
ANSWER = 0

# visited
visited = [False] * N

# permutation
permutation([], NUMBER)
print(ANSWER)