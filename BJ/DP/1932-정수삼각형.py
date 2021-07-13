"""
<DP>
"""
from sys import *

# INPUT
n = int(stdin.readline().rstrip())
TRIANGLE = [[]]
for _ in range(n):
    TRIANGLE.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(2, n + 1):  # 2 ~ n
    for j in range(i):  # 0 ~ i
        if j == 0:
            TRIANGLE[i][j] += TRIANGLE[i - 1][j]
        elif j == i - 1:
            TRIANGLE[i][j] += TRIANGLE[i - 1][j - 1]
        else:
            TRIANGLE[i][j] += max(TRIANGLE[i - 1][j - 1], TRIANGLE[i - 1][j])

print(max(TRIANGLE[n]))
