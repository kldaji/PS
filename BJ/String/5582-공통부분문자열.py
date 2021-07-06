"""
<String>
<Dynamic Programming>
"""
from sys import *

"""
<Example>
ABRACADABRA vs ECADADABRBCRDARA

   "" E C A D A D A B R B C R D A R A
   -----------------------------------
""| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
A | 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1
B | 0 0 0 0 0 0 0 0 2 0 1 0 0 0 0 0 0
R | 0 0 0 0 0 0 0 0 0 3 0 0 1 0 0 1 0
A | 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 2
C | 0
A | 0
D | 0 
A | 0 
B | 0 
R | 0 
A | 0
"""

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()

dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1

answer = 0
for d in dp:
    temp = max(d)
    answer = max(temp, answer)
print(answer)
