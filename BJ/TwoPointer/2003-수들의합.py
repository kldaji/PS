"""
<Two Pointer>
"""

"""
<INCORRECT>
"""
from sys import *

# N (1 ~ 10,000)
# M (1 ~ 300,000,000)
N, M = map(int, stdin.readline().rstrip().split())

seq = list(map(int, stdin.readline().rstrip().split()))

# two pointer
start = 0
end = 0

total = 0
answer = 0

while not (start == end == N):
    # start ~ end
    if total < M and end < N:
        total += seq[end]
        end += 1
    else:
        total -= seq[start]
        start += 1

    if total == M:
        answer += 1


print(answer)
