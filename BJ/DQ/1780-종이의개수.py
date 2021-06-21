from sys import *

setrecursionlimit(10 ** 6)


def foo(x, y, N):
    global papers, answer

    if N == 1:
        answer[papers[x][y]] += 1
        return

    div = N // 3
    target = papers[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if papers[i][j] != target:
                foo(x, y, div)
                foo(x, y + div, div)
                foo(x, y + div + div, div)
                foo(x + div, y, div)
                foo(x + div + div, y, div)
                foo(x + div, y + div, div)
                foo(x + div + div, y + div, div)
                foo(x + div, y + div + div, div)
                foo(x + div + div, y + div + div, div)
                return

    answer[target] += 1


N = int(stdin.readline().rstrip())

papers = []

# -1, 0, 1
answer = {}
answer[-1] = 0
answer[0] = 0
answer[1] = 0

for _ in range(N):
    papers.append(list(map(int, stdin.readline().rstrip().split())))

foo(0, 0, N)

for count in answer.values():
    print(count)