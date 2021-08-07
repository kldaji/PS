import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if not heap:  # empty
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
