"""
<DP>
<LIS>
"""
from sys import *

# INPUT
N = int(stdin.readline().rstrip())
BUILDING = []
for _ in range(N):
    BUILDING.append(list(map(int, stdin.readline().rstrip().split())))

# A를 기준으로 정렬
BUILDING.sort()

# B에 대해서 LIS(Longest Increasing Subsequence)를 구한다.
# 8 2 9 1 4 6 7 10

dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    for j in range(1, i):
        if BUILDING[i - 1][1] > BUILDING[j - 1][1] and dp[i] < dp[j]:
            # 현재 값보다 작은 값이 있고, dp값이 더 크다면 update를 해준다.
            dp[i] = dp[j]
    # 자기 자신을 포함해야하므로 항상 +1을 해준다.
    dp[i] += 1

print(N - max(dp))
