from sys import *

# 2 x n (1 ~ 1000)
n = int(stdin.readline().rstrip())

"""
<Example>
1) n = 1 : 1개
2) n = 2 : 3개
3) n = 3 : 5개 
4) n = 4 : 11개 

dp[i] = dp[i-1] + 2*dp[i-2]
"""

dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

print(dp[n] % 10007)
