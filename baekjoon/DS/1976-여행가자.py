from sys import *


def get_parent(parent, x):
    if x == parent[x]:
        return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    # a's parent
    a = get_parent(parent, a)
    # b's parent
    b = get_parent(parent, b)

    if a == b:
        return

    # set parent smaller value
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

# 0, 0, 0, ...
parent = [0] * (n + 1)

# 0, 1, 2, 3, ...
for i in range(1, n + 1):
    parent[i] = i

for i in range(1, n + 1):  # 1 ~ n
    # get graph information
    info = list(map(int, stdin.readline().rstrip().split()))

    # information traversal
    for j in range(1, len(info) + 1):  # 1 ~ len(info)
        # connected
        if info[j - 1] == 1:
            union_parent(parent, i, j)

path = list(map(int, stdin.readline().rstrip().split()))
result = set([get_parent(parent, i) for i in path])

if len(result) != 1:
    print("NO")
else:
    print("YES")
