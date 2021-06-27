"""
<String>
"""

from sys import *

# sort by total number
def comp(guitar):
    total = 0
    for g in guitar:
        if g.isdigit():
            total += int(g)
    return total


# number of guitar
N = int(stdin.readline().rstrip())

guitars = []

for _ in range(N):
    guitars.append(stdin.readline().rstrip())

# sort by length, total number, ascending
guitars.sort(key=lambda x: (len(x), comp(x), x))
print("\n".join(guitars))