import heapq
N = int(input())

heap = []

for _ in range(N):
  heapq.heappush(heap, int(input()))

total = 0

while len(heap) != 1:
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)
  heapq.heappush(heap, a+b)
  total += (a+b)

print(total)

"""
<heapq>
- import heapq
- len(heap)
"""
