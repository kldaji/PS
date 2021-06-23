from sys import *

n = int(stdin.readline().rstrip())

# 0 ~ 1000 (list)
dp = [0 for _ in range(1001)]

# n = 1
dp[1] = 1
# n = 2
dp[2] = 2
# n = 3`
dp[3] = 3
# n = 4
dp[4] = 5

# rule : dp[i] = dp[i-1] + dp[i-2]

for i in range(5, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)
