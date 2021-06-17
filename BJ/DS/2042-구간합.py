from sys import stdin, stdout, setrecursionlimit
import math

# setrecursionlimit(5000)

# N : array size
# M : number of update
# K : number of getting range sum
N, M, K = map(int, stdin.readline().rstrip().split())

# array
arr = []

for _ in range(N):
    arr.append(int(stdin.readline().rstrip()))


# tree height
h = int(math.ceil(math.log2(N)))
# tree size : 2^(h+1)
ts = 1 << (h + 1)
# tree
tree = [0]*ts


def init(node, s, e):
    if s == e:
        # leaf node
        tree[node] = arr[s]
        return tree[node]
    else:
        mid = (s + e) // 2
        # 자식 노드 생성
        tree[node] = init(node * 2, s, mid) + init(node * 2 + 1, mid + 1, e)
        return tree[node]


def sum(node, s, e, l, r):
    if l > e or s > r:
        # [l, r]의 범위가 아니다.
        return 0
    if l <= s and e <= r:
        # [l,r]은 [s,e]를 포함한다.
        return tree[node]

    mid = (s + e) // 2
    # 자식 노드 검사
    ret = sum(node * 2, s, mid, l, r) + sum(node * 2 + 1, mid + 1, e, l, r)
    return ret


def update(node, s, e, idx, diff):
    if idx < s or idx > e:
        # idx가 포함되지 않는 범위
        return

    # update
    tree[node] += diff

    if s != e:
        mid = (s + e) // 2
        update(node * 2, s, mid, idx, diff)
        update(node * 2 + 1, mid + 1, e, idx, diff)


# init tree
init(1, 0, N - 1)

# M번 update, K번 get sum
for _ in range(M + K):
    cmd, a, b = map(int, stdin.readline().rstrip().split())

    if cmd == 1:
        a -= 1
        diff = b - arr[a]
        arr[a] = b
        update(1, 0, N - 1, a, diff)
    else:
        print((sum(1, 0, N - 1, a - 1, b - 1)))
