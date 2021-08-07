import heapq

N = int(input())

classes = []

for _ in range(N):
  classes.append(list(map(int, input().split())))

classes.sort(key = lambda x: x[0])

heap = []
heapq.heappush(heap, classes[0][1])

for i in range(1, N):
  if heap[0] <= classes[i][0]:
    heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1])
  else:
    heapq.heappush(heap, classes[i][1])

print(len(heap))


"""
<sort>
- arr.sort(key = lamba x: x[0])
"""
