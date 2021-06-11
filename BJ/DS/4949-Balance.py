import sys

while True:
    stat = list(sys.stdin.readline().rstrip())

    if len(stat) == 1 and stat[0] == ".":
        break

    s = []
    balance = True

    for i in stat:
        if i == "[" or i == "(":
            s.append(i)
        elif i == "]":
            if s and s[-1] == "[":
                s.pop()
            else:
                balance = False
                break
        elif i == ")":
            if s and s[-1] == "(":
                s.pop()
            else:
                balance = False
                break

    if balance and not s:
        print("yes")
    else:
        print("no")
