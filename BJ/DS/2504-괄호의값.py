import sys

stat = sys.stdin.readline().rstrip()

stack = []
possible = True

for s in stat:
    if s == "(" or s == "[":
        stack.append(s)
    elif s == ")":
        if not stack or stack[-1] != "(":
            possible = False
            break
        else:
            stack.pop()
    elif s == "]":
        if not stack or stack[-1] != "[":
            possible = False
            break
        else:
            stack.pop()

if not possible or stack:
    print(0)
else:
    stack = []
    for s in stat:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            temp = 0
            while stack[-1] != "(":
                temp += stack.pop()
            stack.pop()
            if temp:
                stack.append(temp * 2)
            else:
                stack.append(2)
        elif s == "]":
            temp = 0
            while stack[-1] != "[":
                temp += stack.pop()
            stack.pop()
            if temp:
                stack.append(temp * 3)
            else:
                stack.append(3)

    answer = 0

    while stack:
        answer += stack.pop()

    print(answer)
