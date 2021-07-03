"""
<Brute Force>
"""
from sys import *

"""
<Example>
16 1 2 -> 1 vs 2
16 8 9 -> 4 vs 5 -> 2 vs 3 -> 1 vs 2 
1000 20 31 -> 10 vs 16 -> 5 vs 8 -> 3 vs 4
"""


def tournament(N, KIM, LIM):
    ROUND = 1

    while True:
        if (LIM - KIM) == 1 and KIM % 2 == 1 and LIM % 2 == 0:
            # diff : 1
            # KIM is odd
            # LIM is even
            return ROUND

        KIM = (KIM + 1) // 2
        LIM = (LIM + 1) // 2
        ROUND += 1
        N //= 2

    return -1


N, KIM, LIM = map(int, stdin.readline().rstrip().split())

# suppose that KIM is always smaller than LIM
if KIM > LIM:
    temp = KIM
    KIM = LIM
    LIM = temp


print(tournament(N, KIM, LIM))