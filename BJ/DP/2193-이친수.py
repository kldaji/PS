from sys import *

# 0으로 시작하지 않는다.
# 1이 반복되지 않는다.

# 1 ~ 90
N = int(stdin.readline().rstrip())

"""
<Example>
1) N = 1 : 1 (1개)
2) N = 2 : 10 (1개)
3) N = 3 : 100, 101 (2개)
4) N = 4 : 1000, 1010, 1001 (3개)
5) N = 5 : 10000, 10100, 10101, 10010, 10001 (5개)

dp[i] = dp[i-2] + dp[i-1]
"""

dp = [0 for _ in range(91)]

dp[1] = 1
dp[2] = 1

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])