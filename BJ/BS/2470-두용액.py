"""
<Binary Search> ???
<Two Pointer>
"""
from sys import *

"""
<Example>
-2 4 -99 -1 98

-99 -2 -1 4 98

-99 + 98 = -1 (negative)
-2 + 98 = 96 (positive)
-2 + 4 = 2 (positive)
-2 + -1 = -3 (negative)
"""
# N (1 ~ 100,000)
N = int(stdin.readline().rstrip())

# solution
SOLUTION = list(map(int, stdin.readline().rstrip().split()))

SOLUTION.sort()

left = 0
right = N - 1
# two solution & mix value
answer = [0, 0, maxsize]


while left < right:
    mix = SOLUTION[left] + SOLUTION[right]

    # close to zero
    if abs(mix) < answer[2]:
        answer[0] = SOLUTION[left]
        answer[1] = SOLUTION[right]
        answer[2] = abs(mix)

    if mix < 0:
        # negative
        left += 1
    elif mix > 0:
        # positive
        right -= 1
    elif mix == 0:
        break

print(answer[0], end=" ")
print(answer[1])
