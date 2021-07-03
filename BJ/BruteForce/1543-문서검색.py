"""
<Brute Force>
"""
from sys import *

DOCUMENT = stdin.readline().rstrip()
string = stdin.readline().rstrip()


ANSWER = 0
i = 0
while i <= len(DOCUMENT) - len(string):
    if DOCUMENT[i : i + len(string)] == string:
        ANSWER += 1
        i += len(string)
    else:
        i += 1

print(ANSWER)