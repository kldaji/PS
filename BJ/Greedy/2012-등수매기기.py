"""
<Greedy>
"""
from sys import *

"""
<Example>
1 5 3 1 2 

1 1 2 3 5
1 2 3 4 5

1 + 1 + 1 = 3
"""
# N (1 ~ 500,000)
N = int(stdin.readline().rstrip())

STUDENT = []
for _ in range(N):
    STUDENT.append(int(stdin.readline().rstrip()))

STUDENT.sort()

DISCONTENT = 0

for i in range(len(STUDENT)):
    DISCONTENT += abs(STUDENT[i] - (i + 1))

print(DISCONTENT)
