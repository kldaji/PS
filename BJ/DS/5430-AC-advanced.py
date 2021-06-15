from sys import stdin, stdout


def AC(cmds, n, li):
    cmds.replace("RR", "")  # Ignore RR
    l, r, dir = 0, 0, True  # True : Left, False : Right

    for cmd in cmds:
        if cmd == "R":
            dir = not dir
        else:
            if dir:
                l += 1
            else:
                r += 1

    if l + r > n:  # D error
        return "error\n"
    else:
        res = li[l : n - r]
        if dir:
            return "[" + ",".join(res) + "]\n"
        else:
            return "[" + ",".join(res[::-1]) + "]\n"


T = int(stdin.readline())

for _ in range(T):
    cmds = stdin.readline().rstrip()
    n = int(stdin.readline().rstrip())
    li = stdin.readline().rstrip()[1:-1].split(",")
    if n == 0:
        li = []
    stdout.write(AC(cmds, n, li))