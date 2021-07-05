"""
<BackTracking>
"""
from sys import *

# natural number N, M (1 ~ 8)
N, M = map(int, stdin.readline().rstrip().split())


def foo(start, LIST):
    if len(LIST) == M:
        print(" ".join(map(str, LIST)))
        return

    for i in range(start + 1, N + 1):
        LIST.append(i)
        foo(i, LIST)
        LIST.pop()


foo(0, [])
