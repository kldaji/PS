"""
<Math>
<Eratosthenes' sieve>
"""
from sys import *

# max number
MAX = 10001

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

T = int(stdin.readline().rstrip())

for i in range(T):
    n = int(stdin.readline().rstrip())

    # answer
    answer = (0, 0)

    # find
    for i in range(2, n // 2 + 1):
        if i in PRIME and n - i in PRIME:
            # both are prime numbers
            answer = (i, n - i)

    print(f"{answer[0]} {answer[1]}")
