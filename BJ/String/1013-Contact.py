"""
<String>
"""

from sys import *
import re

"""
<특이점>
m.group() 함수를 사용하면 Attribute Error가 뜬다.
"""

# test case
T = int(stdin.readline().rstrip())

for _ in range(T):
    string = stdin.readline().rstrip()

    # regular expression
    p = re.compile("(100+1+|01)+")

    m = p.fullmatch(string)
    if m:
        print("YES")
    else:
        print("NO")
