"""
<Greedy>
"""

"""
<Example>
B -> BA -> ABB -> ABBA
AB -> BAB (X)
"""

"""
<INCORRECT>
"""
from sys import *

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()

i = 0
while len(S) != len(T):
    if i < len(S) and S[i] == T[i]:
        i += 1
        continue

    if T[i] == "A":
        S += "A"
    else:
        S = S[::-1]
        S += "B"
    i += 1

if S == T:
    print(1)
else:
    print(0)