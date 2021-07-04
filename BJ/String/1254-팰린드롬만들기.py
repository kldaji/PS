"""
<String>
<Brute Force>
"""
from sys import *

# string
S = stdin.readline().rstrip()

"""
S[len(S) - 1 : i - 1 : -1] -> 0 일때 공백만 출력되서
S == S[::-1] 조건을 따로 두었다.

하지만 이를 해결하기 위한 방법 : 
S[i:][::-1]을 사용하면 된다.
"""
if S == S[::-1]:
    print(len(S))
else:
    # find palindrome
    for i in range(1, len(S)):
        if S[i:] == S[len(S) - 1 : i - 1 : -1]:
            S += S[i - 1 :: -1]
            break

    print(len(S))


# for i in range(len(S)):
#     print(S[i:][::-1])
#     if S[i:] == S[i:][::-1]:
#         print(len(S) + i)
#         break