# Binary Search

from sys import *


def binary_search(l, r, target):
    global nums

    if l > r:
        return False

    mid = (l + r) // 2

    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return binary_search(mid + 1, r, target)
    else:
        return binary_search(l, mid - 1, target)


N = int(stdin.readline().rstrip())

nums = list(map(int, stdin.readline().rstrip().split()))
nums.sort()

M = int(stdin.readline().rstrip())

targets = list(map(int, stdin.readline().rstrip().split()))

for target in targets:
    if binary_search(0, N - 1, target):
        print(1)
    else:
        print(0)
