from sys import *

S = int(stdin.readline().rstrip())

# SUM
total = 1

# 자연수
number = 1

# S보다 커질 때까지 진행
while True:
    number += 1
    total += number

    if total > S:
        break


# 바로 전 숫자가 정답
print(number - 1)
