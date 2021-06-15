from sys import stdin, stdout
import heapq

n, m = map(int, stdin.readline().rstrip().split())

heap = []

wb = [[] for i in range(n + 1)]  # work book
degree = [0 for i in range(n + 1)]  # 0번째 index는 사용하지 않는다.

for i in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    wb[a].append(b)  # a -> b
    degree[b] += 1  # 차수

for i in range(1, n + 1):
    if degree[i] == 0:  # 차수가 0인 문제 push
        heapq.heappush(heap, i)

answer = []

# 위상 정렬
while heap:
    problem = heapq.heappop(heap)
    answer.append(problem)

    for i in range(len(wb[problem])):
        temp = wb[problem][i]  # 다음 문제 후보
        degree[temp] -= 1

        if degree[temp] == 0:  # OK
            heapq.heappush(heap, temp)


print(" ".join(map(str, answer)))
