"""
<DP>
"""
from sys import *

n = int(stdin.readline().rstrip())

dp = [0] * 91


def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1

    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo(x - 1) + fibo(x - 2)
    return dp[x]


print(fibo(n))