"""
<Bit Masking>
"""

from sys import *

# X
X = int(stdin.readline().rstrip())

answer = 0

while X != 0:
    # find 1
    if X & 1:
        answer += 1
    X = X >> 1

print(answer)
