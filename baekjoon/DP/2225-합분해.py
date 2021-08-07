"""
<DP>
"""
from sys import *

"""
dp[i][j] -> j개를 더해서 i가 되는 경우의수

  0 1 2 3 4 5 6 7 8 9 
0 0 0 0 0 0 0 0 0 0 0
1 0 1 2 3 4 5 6 7 8 9
2 0 1 3 6 10
3 0 1 4 10 20
4 0 1 5 15
5 0 1 6
6 0 1 7
7 0 1
8 0 1
9 0 1
"""
# INPUT
N, K = map(int, stdin.readline().rstrip().split())

# DP
dp = [[0] * 201 for _ in range(201)]
for i in range(201):
    dp[i][1] = 1
for j in range(2, 201):
    dp[1][j] = j

for i in range(2, N + 1):
    for j in range(2, K + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

print(dp[N][K])