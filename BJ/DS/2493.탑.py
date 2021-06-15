from sys import stdin, stdout

n = int(stdin.readline())
tops = list(map(int, stdin.readline().rstrip().split()))

stack = []
answer = []

for i in range(n):

    while stack:
        if tops[i] < stack[-1][1]:  # detect top
            answer.append(stack[-1][0] + 1)
            break
        else:  # unnecessary
            stack.pop()

    if not stack:  # empty
        answer.append(0)
    stack.append([i, tops[i]])

print(" ".join(map(str, answer)))
