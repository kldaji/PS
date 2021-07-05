"""
<Greedy>
<Priority Queue>
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

# list
LECTURE = []
for _ in range(N):
    P, D = map(int, stdin.readline().rstrip().split())
    LECTURE.append((P, D))

# day : ascending
LECTURE.sort(key=lambda x: x[1])

for money, day in LECTURE:
    # priority queue
    heapq.heappush(HEAP, money)

    # len(HEAP) : number of lecture
    if len(HEAP) > day:
        # pop less money
        heapq.heappop(HEAP)

print(sum(HEAP))
