"""
<DP>
"""
from sys import *

# INPUT
N = int(stdin.readline().rstrip())
NUMBER = list(map(int, stdin.readline().rstrip().split()))

# i번째 인덱스까지 계산했을 때 j라는 값이 나오는 경우의 수
dp = [[0] * 21 for _ in range(N)]

# 0번째 인덱스까지 계산했을 때 NUMBER[0]이라는 값이 나오는 경우의 수는 한 가지
dp[0][NUMBER[0]] = 1

# 1 ~ N-2번째 인덱스 탐색
for i in range(1, N - 1):
    for j in range(21):
        # i-1번째 인덱스까지 계산한 값이 0 ~ 20이라는 값으로 나왔을 때만 확인
        if dp[i - 1][j]:
            if 0 <= j + NUMBER[i] <= 20:
                dp[i][j + NUMBER[i]] += dp[i - 1][j]
            if 0 <= j - NUMBER[i] <= 20:
                dp[i][j - NUMBER[i]] += dp[i - 1][j]

# N-2번째 인덱스까지 계산했을 때 NUMBER[-1]의 값이 나오는 경우의 수
print(dp[N - 2][NUMBER[-1]])
