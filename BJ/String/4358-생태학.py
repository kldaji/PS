"""
<String>
<Hash>
"""
from sys import *
from collections import defaultdict

TREE = defaultdict(int)
num = 0
while True:
    tree = stdin.readline().rstrip()

    if not tree:
        break

    TREE[tree] += 1
    num += 1

TREE_LIST = sorted(TREE.keys())

for tree in TREE_LIST:
    print("%s %.4f" % (tree, TREE[tree] / num * 100))
