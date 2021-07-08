"""
<Math>
"""
from sys import *
from math import factorial

N, K = map(int, stdin.readline().rstrip().split())

ans = factorial(N) // (factorial(K) * factorial(N - K))
print(ans % 10007)


"""
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
...

dp = [[0] for _ in range(1002)]

dp[1].append(1)

for i in range(2, 1002):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])


print(dp[N + 1][K + 1] % 10007)
"""