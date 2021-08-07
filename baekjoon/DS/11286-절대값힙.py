import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
