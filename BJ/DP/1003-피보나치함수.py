from sys import *

# test cast
T = int(stdin.readline().rstrip())

# dp (0 ~ 40)
dp = [[0, 0] for _ in range(41)]

# N = 0
dp[0][0] = 1
dp[0][1] = 0

# N = 1
dp[1][0] = 0
dp[1][1] = 1

# N = 2
dp[2][0] = 1
dp[2][1] = 1

# N = 3
dp[3][0] = 1
dp[3][1] = 2

for i in range(4, 41):
    # rule
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]


for _ in range(T):
    # integer
    N = int(stdin.readline().rstrip())
    print(dp[N][0], end=" ")
    print(dp[N][1])