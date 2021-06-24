from sys import *

"""
<오답>
"""
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


# 1th
first = 1
# 2th
second = 2

# temporary storage
temp = 1

for i in range(N - 1):
    temp = first
    first = second

    # first + second
    second = temp + second

print(first % 15746)