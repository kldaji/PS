"""
<Brute Force>
"""
from sys import *


def permutation(LIST):
    if len(LIST) == N:
        print(" ".join(map(str, LIST)))
        return

    for i in range(1, N + 1):
        if i not in LIST:
            LIST.append(i)
            permutation(LIST)
            LIST.remove(i)


# N (1 ~ 8)
N = int(stdin.readline().rstrip())

permutation([])
