"""
<Greedy>
<Priority Queue>
"""

"""
<INCORRECT>
"""

"""
<Example>
20 1, 2 1, 10 3, 100 2, 8 2, 5 20, 50 10
1 20 vs 1 2 (20)
2 100 vs 2 8 (100)
3 10 (10)
10 50 (50)
20 5 (5)
"""
from sys import * 
import heapq

# N (0 ~ 10,000)
N = int(stdin.readline().rstrip())

# heap
HEAP = []

for _ in range(N):
    P, D = map(int, stdin.readline().rstrip().split())
    # D : ascending
    # P : desceding
    heapq.heappush(HEAP, (-P, D))

# start
DAY = 1

# answer
ANSWER = 0

# loop until empty
while HEAP:
    P, D = heapq.heappop(HEAP)
    P = -P

    if D >= DAY:
        ANSWER += P
        DAY += 1

print(ANSWER)
