"""
<DP>
"""
from sys import *

# INPUT
n = int(stdin.readline().rstrip())
SEQ = list(map(int, stdin.readline().rstrip().split()))

SUM = []
SUM.append(SEQ[0])

# 누적된 값에 현재 인덱스 값을 더한 값과 현재 인덱스 값을 비교한다.
for i in range(n - 1):
    SUM.append(max(SUM[i] + SEQ[i + 1], SEQ[i + 1]))

print(max(SUM))