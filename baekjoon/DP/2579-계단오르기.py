from sys import *

# steps
N = int(stdin.readline().rstrip())

# 0 ~ N-1
scores = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(N):
    scores[i] = int(stdin.readline().rstrip())

# 0
dp[0] = scores[0]
# 0+1
dp[1] = scores[0] + scores[1]
# 0+2 or 1+2
dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

"""
4번째를 기준으로 생각해보면
1, 3, 4 vs 1, 2, 4 
dp[4-1] + scores[3] + scores[4]
dp[2] + scores[4]
"""

for i in range(3, N):
    # rule
    dp[i] = max(dp[i - 3] + scores[i - 1] + scores[i], dp[i - 2] + scores[i])

print(dp[N - 1])
