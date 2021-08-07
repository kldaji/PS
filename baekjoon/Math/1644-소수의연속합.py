"""
<Math>
<Eratosthenes' sieve>
<Two Pointer>
"""
from sys import *

# N : 1 ~ 4000000
N = int(stdin.readline().rstrip())

# check wether prime or not
CHECK = [True] * (4000001)

# init
CHECK[1] = False
CHECK[2] = True

# prime list
PRIME = []

for i in range(2, 4000001):
    if CHECK[i]:
        # prime
        PRIME.append(i)

        # check false not prime number
        for j in range(i * 2, 4000001, i):
            CHECK[j] = False

s = 0  # start
e = 0  # end
ANSWER = 0  # answer
TOTAL = 0  # total

while not (s == e == len(PRIME)):
    if TOTAL < N and e < len(PRIME):
        TOTAL += PRIME[e]
        e += 1
    else:
        TOTAL -= PRIME[s]
        s += 1

    if TOTAL == N:
        ANSWER += 1

print(ANSWER)