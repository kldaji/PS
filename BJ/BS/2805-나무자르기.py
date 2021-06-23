# Binary Search

from sys import *


def cut_tree(low, high):
    global trees, M, answer

    while low <= high:
        # middle value
        mid = (low + high) // 2

        total = 0

        # cutting
        for tree in trees:
            if tree > mid:
                # can cut
                total += tree - mid

        if total >= M:
            # max value
            answer = max(answer, mid)

            # more
            low = mid + 1
        else:
            # less
            high = mid - 1


N, M = map(int, stdin.readline().rstrip().split())

# get trees
trees = list(map(int, stdin.readline().rstrip().split()))

# answer
answer = 0

# sort
trees.sort()

cut_tree(0, trees[-1])

print(answer)