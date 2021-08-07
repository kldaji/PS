"""
<Dynamic Programming>
"""
from sys import *

# 자연수 N(1 ~ 1000000)
N = int(stdin.readline().rstrip())

"""
<Example>
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
dp[5] = 8
dp[6] = 13
"""

# N = 1
first = 1
second = 2

# N = 2 ~
for i in range(2, N + 1):
    temp = first
    first = second

    # first + second
    second = (temp + second) % 15746

print(first)

# mod를 계산 중에 하는 것이 시간초과를 해결했다..
# mod가 시간에도 영향을 끼치나..?