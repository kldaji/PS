from sys import *
from collections import Counter

n = int(stdin.readline().rstrip())

cards = []

for _ in range(n):
    num = int(stdin.readline().rstrip())
    cards.append(num)

num_count = Counter(cards)

# sort counter (convert to list)
num_count = sorted(num_count.items(), key=lambda x: (-x[1], x[0]))


print(num_count[0][0])