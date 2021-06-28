"""
<String>
"""

from sys import *

"""
<오답>
"""


"""
<Example>
ABRACADABRA vs ECADADABRBCRDARA

   "" E C A D A D A B R B C R D A R A
   -----------------------------------
""| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
A | 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 1
B | 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0
R | 0 0 0 0 0 0 0 0 0 0 0 0 1 
A | 0 0 0 1 1 1 1 1 2 3 3 3 3 3 3 3 3
C | 0 0 1 1 1 1 1 1 2 3 3 3 3 3 3 3 3 
A | 0 0 1 2 2 2 2 2 2 3 3 3 3 3 3 3 3
D | 0 0 1 2 3 3 3 3 3 3 3 3 3 3 3 3 3
A | 0 0 1 2 3 3 3 3 3 3 3 3 3 3 3 3 3 
B | 0 0 1 2 3 3 3 3 4 4 4 4 4 4 4 4 4
R | 0 0 
A | 0
"""

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()

dp = [[0] * (len(s2)) for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] != s2[j]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else:
            if s1[i - dp[i - 1][j - 1] : i + 1] in s2[:j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(s1) - 1][len(s2) - 1])
