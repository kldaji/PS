from sys import *


def comp_number(numbers):
    for i in range(len(numbers) - 1):
        length = len(numbers[i])
        if numbers[i] == numbers[i + 1][:length]:
            return False

    return True


T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())

    numbers = []

    for _ in range(N):
        numbers.append(stdin.readline().strip())

    numbers.sort()

    if comp_number(numbers):
        print("YES")
    else:
        print("NO")
