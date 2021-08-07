from sys import *

# N
N = int(stdin.readline().rstrip())

grape = [0 for _ in range(10001)]
dp = [0 for _ in range(10001)]

for i in range(N):
    grape[i] = int(stdin.readline().rstrip())

dp[0] = grape[0]
dp[1] = grape[0] + grape[1]
dp[2] = max(grape[0] + grape[2], grape[1] + grape[2], grape[0] + grape[1])

"""
<경우의 수는 3가지> - ex) 3
1) dp[2] : pass
2) dp[0] + grape[2] + grape[3] 
3) dp[1] + grape[3]
"""
for i in range(3, N):
    dp[i] = max(dp[i - 1], dp[i - 3] + grape[i - 1] + grape[i], dp[i - 2] + grape[i])

# Get max dp
print(max(dp))