from sys import *

# N
N = int(stdin.readline().rstrip())

# sequences
seqs = list(map(int, stdin.readline().rstrip().split()))

# 0 ~ 1000, default value = 1
dp = [1 for _ in range(1001)]

for i in range(1, N):
    # 0 ~ i-1
    for j in range(i):
        if seqs[i] > seqs[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
