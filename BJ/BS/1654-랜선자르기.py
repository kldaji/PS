"""
<Binary Search>
"""
from sys import *

# K : LAN already has (1 ~ 10,000)
# N : needed LAN (1 ~ 1,000,000)
K, N = map(int, stdin.readline().rstrip().split())

LAN = []

for _ in range(K):
    LAN.append(int(stdin.readline().rstrip()))

left = 1
right = max(LAN)
ANSWER = 0

while left <= right:
    mid = (left + right) // 2

    total = 0

    for lan in LAN:
        total += lan // mid

    if total >= N:
        ANSWER = max(ANSWER, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ANSWER)