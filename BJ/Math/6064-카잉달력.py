"""
<Math>
"""
from sys import *

T = int(stdin.readline().rstrip())

for _ in range(T):
    M, N, x, y = map(int, stdin.readline().rstrip().split())

    year = 0

    while x <= M * N:
        if (x - y) % N == 0:
            year = x
            break
        x += M

    print(-1) if year == 0 else print(year)
