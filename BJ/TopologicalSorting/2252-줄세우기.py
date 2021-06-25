"""
<Topological sorting>
"""

from sys import *
import heapq

# number of students (1 ~ 32,000)
# number of compare (1 ~ 100,000)
N, M = map(int, stdin.readline().rstrip().split())

degrees = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    # A < B
    A, B = map(int, stdin.readline().rstrip().split())
    degrees[B] += 1
    graph[A].append(B)

heap = []

for i in range(1, N + 1):
    # find degree 0
    if not degrees[i]:
        heapq.heappush(heap, i)

while heap:
    student = heapq.heappop(heap)
    print(student, end=" ")

    for next in graph[student]:
        degrees[next] -= 1
        if not degrees[next]:
            heapq.heappush(heap, next)