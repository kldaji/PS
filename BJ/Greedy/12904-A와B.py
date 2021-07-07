"""
<Greedy>
"""
from sys import *

S = stdin.readline().rstrip()
T = list(stdin.readline().rstrip())

# Core thing is thinking backwards

# backwards
for i in range(len(T) - 1, len(S) - 1, -1):
    if T[i] == "A":
        T.pop()
    elif T[i] == "B":
        T.pop()
        T = T[::-1]

if "".join(T) == S:
    print(1)
else:
    print(0)