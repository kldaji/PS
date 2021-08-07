from sys import *

T = int(stdin.readline().rstrip())

# 0 ~ 10
dp = [0 for _ in range(11)]

dp[0] = 0
# 1
dp[1] = 1
# 1+1, 2
dp[2] = 2
# 1+1+1, 1+2, 2+1, 3
dp[3] = 4

# rule : dp[i] = dp[i-3] + dp[i-2] + d[i-1]
for i in range(4, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(T):
    n = int(stdin.readline().rstrip())
    print(dp[n])
