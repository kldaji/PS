"""
<Math>
<Eratosthenes' sieve>
"""
from sys import *

# max number
MAX = 1000001

# check wether prime or not
CHECK = [True] * MAX

# init
CHECK[1] = False
CHECK[2] = True

# prime set
PRIME = set()

for i in range(2, MAX):
    if CHECK[i]:
        # prime
        PRIME.add(i)

        # check false not prime number
        for j in range(i * 2, MAX, i):
            CHECK[j] = False

N, M = map(int, stdin.readline().rstrip().split())

for i in range(N, M + 1):
    if i in PRIME:
        print(i)