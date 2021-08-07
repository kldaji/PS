"""
<String>
"""

from sys import *
from collections import Counter

N = int(stdin.readline().rstrip())

books = []

for _ in range(N):
    books.append(stdin.readline().rstrip())

# Count
res = Counter(books)

# get max
best = max(res.values())

# get only bestseller books
res = list(filter(lambda x: x[1] == best, res.items()))

# ascedning order
res.sort()

# print book title only
print(res[0][0])