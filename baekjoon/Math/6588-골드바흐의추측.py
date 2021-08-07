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

while True:
    n = int(stdin.readline().rstrip())

    if n == 0:
        break

    for i in range(2, n):
        if i in PRIME and n - i in PRIME:
            # both are prime numbers
            print(f"{n} = {i} + {n-i}")
            break
