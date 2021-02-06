import heapq

N, M = map(int, input().split())

scores = list(map(int, input().split()))

heap = []

for score in scores:
  heapq.heappush(heap, score)

for _ in range(M):
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)
  heapq.heappush(heap, a+b)
  heapq.heappush(heap, a+b)


print(sum(heap))

"""
<priority queue>
- import heapq
- heappush
- heappop
"""
