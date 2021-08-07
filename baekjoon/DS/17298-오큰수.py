from sys import *

N = int(stdin.readline().rstrip())

numbers = list(map(int, stdin.readline().rstrip().split()))

stack = []
answer = [-1 for _ in range(N)]

# 0번째 index 추가
stack.append(0)

# index 1번부터 시작
i = 1

while stack and i < N:
    while stack and numbers[stack[-1]] < numbers[i]:
        # 오큰수 발견
        answer[stack[-1]] = numbers[i]
        stack.pop()

    stack.append(i)
    i += 1

for i in range(N):
    print(answer[i], end=" ")
