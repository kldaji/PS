from sys import *

# N
N = int(stdin.readline().rstrip())

# 0 ~ 10^6 (list)
dp = [maxsize for _ in range(1000001)]

# default value
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    # divided by 2
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # divided by 2
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[N])