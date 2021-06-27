"""
<String>
"""

from sys import *

"""
c=, c-, dz=, d-, lj, nj, s=, z=
"""

S = stdin.readline().rstrip()

words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

cnt = 0

for word in words:
    cnt += S.count(word)

print(len(S) - cnt)
