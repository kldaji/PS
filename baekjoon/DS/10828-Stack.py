import sys

n = int(sys.stdin.readline().rstrip())
stack = []
top = -1

for i in range(n):
    cmd = sys.stdin.readline().rstrip()

    keys = cmd.split(" ")

    if keys[0] == "push":
        stack.append(keys[1])
        top += 1
    elif keys[0] == "top":
        if top != -1:
            print(stack[top])
        else:
            print(-1)
    elif keys[0] == "size":
        print(len(stack))
    elif keys[0] == "empty":
        if top != -1:
            print(0)
        else:
            print(1)
    elif keys[0] == "pop":
        if top != -1:
            value = stack.pop()
            print(value)
            top -= 1
        else:
            print(-1)

"""
<TIME OUT>
Try to use sys...!!!
Always...
"""
