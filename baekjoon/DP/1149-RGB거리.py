from sys import *

# N
N = int(stdin.readline().rstrip())

# house list
houses = []

# house info
for _ in range(N):
    houses.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(1, N):
    houses[i][0] = min(houses[i - 1][1] + houses[i][0], houses[i - 1][2] + houses[i][0])
    houses[i][1] = min(houses[i - 1][0] + houses[i][1], houses[i - 1][2] + houses[i][1])
    houses[i][2] = min(houses[i - 1][0] + houses[i][2], houses[i - 1][1] + houses[i][2])

print(min(houses[N - 1]))
