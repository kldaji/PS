from sys import *

setrecursionlimit(10 ** 6)


def foo(x, y, N):
    global count, r, c

    if N == 2:
        for i in range(x, x + 2):
            for j in range(y, y + 2):
                if i == r and j == c:
                    print(count)
                    exit(0)
                count += 1
        return

    if not (x <= r < x + N and y <= c < y + N):
        count += N * N
        return

    div = N // 2

    for i in range(2):
        for j in range(2):
            foo(x + i * div, y + j * div, div)


N, r, c = map(int, stdin.readline().rstrip().split())

N = 1 << N

count = 0

foo(0, 0, N)
