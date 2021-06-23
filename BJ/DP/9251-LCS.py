from sys import *

"""
   0 A C A Y K P
----------------
0| 0 0 0 0 0 0 0
C| 0 0 1 1 1 1 1
A| 0 1 1 2 2 2 2
P| 0 1 1 2 2 2 3
C| 0 1 2 2 2 2 3
A| 0 1 2 3 3 3 3
K| 0 1 2 3 3 4 4

<rule>
1) same alphabet : dp[i][j] = dp[i-1][j-1] + 1
2) different alphabet : dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 
"""

# get strings
string1 = stdin.readline().rstrip()
string2 = stdin.readline().rstrip()

# (len(string1) + 1) X (len(string2) + 1), default value = 0
dp = [[0] * (len(string2) + 1) for _ in range((len(string1) + 1))]

# 1 ~ len(string1), 1 ~ len(string2)
for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        # rule
        if (
            string1[i - 1] == string2[j - 1]
        ):  # dp : starts with 1, string : starts with 0
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print max dp (in 2-dimension)
print(max(max(dp)))
