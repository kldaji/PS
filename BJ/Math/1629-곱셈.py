"""
<Math>
"""
from sys import *

"""
EVEN : C^n = C^(n//2) * C^(n//2)
ODD : C^n = C^((n-1)//2) * C^((n-1)//2) * C
-> same as C^(n//2) * C^(n//2) * C 
"""

# def dc(a, b, c):
#     if b == 1:
#         return a % c

#     ret = dc(a, b // 2, c)
#     if b % 2 == 0:
#         return ret * ret % c
#     else:
#         return ret * ret * a % c


A, B, C = map(int, stdin.readline().rstrip().split())

print(pow(A, B, C))
# print(dc(A, B, C))
