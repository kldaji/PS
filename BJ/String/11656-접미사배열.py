from sys import *

word = stdin.readline().rstrip()

suffixes = []

for i in range(len(word)):
    suffixes.append(word[i:])

suffixes.sort()

for suffix in suffixes:
    print(suffix)