from sys import *
import math


def init(arr, tree, node, s, e):
    if s == e:
        # (min, max)
        tree[node] = (arr[s], arr[s])
        return tree[node]
    else:
        mid = (s + e) // 2

        left = init(arr, tree, node * 2, s, mid)
        right = init(arr, tree, node * 2 + 1, mid + 1, e)

        tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
        return tree[node]


def query(arr, tree, node, s, e, l, r):
    if l > e or r < s:
        return (maxsize, 0)
    if l <= s and r >= e:
        return tree[node]

    mid = (s + e) // 2

    left = query(arr, tree, node * 2, s, mid, l, r)
    right = query(arr, tree, node * 2 + 1, mid + 1, e, l, r)

    ret = (min(left[0], right[0]), max(left[1], right[1]))
    return ret


n, m = map(int, stdin.readline().rstrip().split())

arr = []

# tree height
h = int(math.ceil(math.log2(n)))
# tree size : 2^(h+1)
ts = 1 << (h + 1)
# tree
tree = [0] * ts

for _ in range(n):
    num = int(stdin.readline().rstrip())
    arr.append(num)

init(arr, tree, 1, 0, n - 1)

for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    ret = query(arr, tree, 1, 0, n - 1, a - 1, b - 1)
    print(ret[0], end=" ")
    print(ret[1])
