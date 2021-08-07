"""
<Math>
<Divide and Conquer>
"""
from sys import *

MOD = 1000000
PERIOD = MOD // 10 * 15

FIBO = [0] * PERIOD
FIBO[1] = 1

for i in range(2, PERIOD):
    FIBO[i] = (FIBO[i - 2] + FIBO[i - 1]) % MOD

N = int(stdin.readline().rstrip())

print(FIBO[N % PERIOD])
