"""
<BackTracking>
"""
from sys import *


def foo(seq):
    global N, M
    if len(seq) == M:
        for s in seq:
            print(s, end=" ")
        print()
        return

    for i in range(1, N + 1):
        if i not in seq:
            seq.append(i)
            foo(seq)
            seq.remove(i)


# natural number N, M (1 ~ 8)
N, M = map(int, stdin.readline().rstrip().split())

answer = []
foo([])


"""
<permutations>

from itertools import permutations

N, M = map(int, input().split())

# iter(tuple)
P = permutations(range(1, N+1), M) 

for i in P:
    # tuple -> str
    print(' '.join(map(str, i)))
"""