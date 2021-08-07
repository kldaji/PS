"""
<DP>
"""
from sys import *

# INPUT
N = int(stdin.readline().rstrip())
CARD = list(map(int, stdin.readline().rstrip().split()))

# DP
dp = [0] * (N + 1)

# 1개를 뽑았을 때의 최대값
dp[1] = CARD[0]

for i in range(2, N + 1):
    # i개를 뽑았을 때의 최대값
    for j in range(1, i):
        """
        예를 들어 4개를 뽑았을 때의 최대값은
        dp[4] = max(dp[3] + CARD[0], CARD[4], dp[4])
        dp[4] = max(dp[2] + CARD[1], CARD[4], dp[4])
        dp[4] = max(dp[1] + CARD[2], CARD[4], dp[4])
        """
        dp[i] = max(dp[i - j] + CARD[j - 1], CARD[i - 1], dp[i])

print(dp[N])