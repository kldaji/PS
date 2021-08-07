from sys import *

setrecursionlimit(10 ** 6)


def foo(x, y, N):
    global answer, quad

    if N == 1:
        answer += quad[x][y]
        return

    target = quad[x][y]
    div = N // 2

    for i in range(x, x + N):
        for j in range(y, y + N):
            if quad[i][j] != target:
                answer += "("
                foo(x, y, div)
                foo(x, y + div, div)
                foo(x + div, y, div)
                foo(x + div, y + div, div)
                answer += ")"
                return

    answer += target


N = int(stdin.readline().rstrip())

quad = []
answer = ""

for _ in range(N):
    quad.append(list(stdin.readline().rstrip()))

foo(0, 0, N)

print(answer)