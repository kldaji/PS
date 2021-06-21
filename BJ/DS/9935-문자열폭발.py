from sys import *

strings = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()

# 스택
stack = []

for string in strings:
    stack.append(string)

    if len(stack) >= len(bomb) and stack[-1] == bomb[-1]:
        # bomb 길이보다 크고, 마지막 글자가 같을 때만 check
        if "".join(stack[-len(bomb) :]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))

"""
<TIME OUT>

while True:
    if bomb in strings:
        strings = strings.replace(bomb, "")
    else:
        break

if strings != "":
    print(strings)
else:
    print("FRULA")
"""