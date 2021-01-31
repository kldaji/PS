from itertools import combinations
import sys

N, M = map(int, input().split())

chicken = []
city = []
house = []

for i in range(N):
  city.append(list(map(int, input().split())))
  for j in range(N):
    if city[i][j] == 2:
      chicken.append([i,j])
    elif city[i][j] == 1:
      house.append([i,j])

possible = list(combinations(chicken, M))

ans = sys.maxsize

for poss in possible:
  total = 0
  for h in house:
    dist = sys.maxsize
    for i in range(M):
      temp = abs(h[0] - poss[i][0]) + abs(h[1] - poss[i][1])
      dist = min(temp, dist)
    total += dist
  ans = min(ans, total)

print(ans)

"""
<combination>

items = ['A','B','C','D']

for i in range(1, len(items)):
  print(list(map(''.join, combinations(items, i))))

<max int>

sys.maxsize
"""
