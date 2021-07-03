"""
<Binary Search>
"""
from sys import *


N, C = map(int, stdin.readline().rstrip().split())

HOUSE = [int(stdin.readline().rstrip()) for _ in range(N)]

# ascending
HOUSE.sort()

left = 0
right = max(HOUSE)

ANSWER = 0

while left <= right:
    mid = (left + right) // 2

    # 0th -> install
    cnt = 1
    prev = HOUSE[0]

    for i in range(1, N):
        # condition
        if HOUSE[i] - prev >= mid:
            cnt += 1
            prev = HOUSE[i]

    if cnt >= C:
        ANSWER = max(ANSWER, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ANSWER)
