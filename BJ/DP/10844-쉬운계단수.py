from sys import *

"""
    0 1 2 3 4 5 6 7 8 9
  ---------------------
1 | 0 1 1 1 1 1 1 1 1 1 
2 | 1 1 2 2 2 2 2 2 2 1
3 | 1 3 3 4 4 4 4 4 3 2 
"""

# 수의 길이 (1 ~ 100)
N = int(stdin.readline().rstrip())

dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i - 1][1]
        elif j == 9:
            dp[i][9] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

# 정답 : 1,000,000,000으로 나눈 나머지.
print(sum(dp[N]) % 1000000000)
