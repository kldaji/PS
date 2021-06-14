import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [i for i in range(n + 1)]


def get_parent(x):
    if x != parent[x]:
        parent[x] = get_parent(parent[x])
    return parent[x]


def union(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    cmd, a, b = map(int, sys.stdin.readline().rstrip().split())

    if cmd == 0:
        union(a, b)
    else:
        if get_parent(a) != get_parent(b):
            print("NO")
        else:
            print("YES")