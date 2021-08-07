from sys import *

# 수의 길이 (1 ~ 1000)
N = int(stdin.readline().rstrip())

"""

<Example> : 0으로 시작할 수 있다.
   0 1 2 3 4 5 6 7 8 9
------------------------
1| 1 1 1 1 1 1 1 1 1 1 
2| 1 2 3 4 5 6 7 8 9 10
3| 1 3 6 ...

dp[i][0] = 1 (always)
dp[i][j] = dp[i-1][j] + dp[i][j-1]
"""

dp = [[0] * (10) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, 10):
        if i == 1:
            dp[i][j] = 1
        else:
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(sum(dp[N]) % 10007)