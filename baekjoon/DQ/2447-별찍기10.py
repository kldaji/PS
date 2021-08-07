from sys import *

setrecursionlimit(10 ** 6)


def fill_star(x, y, N):
    global answer

    if N == 1:
        answer[x][y] = "*"
        return

    div = N // 3

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            fill_star(x + div * i, y + div * j, div)


N = int(stdin.readline().rstrip())

# 전부 공백
answer = [[" " for _ in range(N)] for _ in range(N)]

# 별 채우기
fill_star(0, 0, N)

for i in range(N):
    print("".join(answer[i]))

"""
<GOOD CODE>
def star(i, j):
    while i != 0:
        if i % 3 == 1 and j % 3 == 1:
            stdout.write(" ")
            return

        # 몫
        i //= 3
        j //= 3

    stdout.write("*")


N = int(stdin.readline().rstrip())

for i in range(N):
    for j in range(N):
        star(i, j)
    stdout.write("\n")
"""