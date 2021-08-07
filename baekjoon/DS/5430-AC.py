import sys
import re
from collections import deque


input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    error = False
    direct = 0  # 0 : Left, 1 : Right

    cmds = input().strip()
    n = int(input().strip())
    arr = re.split("\[|\]|,", input().strip())
    arr = deque(filter(None, arr))

    for cmd in cmds:
        if cmd == "R":
            direct = not direct
        else:
            if arr:
                if direct:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print("error")
                error = True
                break

    if not error:
        print("[", end="")
        if not direct:
            for i in range(len(arr)):
                print(arr[i], end="")
                if i < len(arr) - 1:
                    print(",", end="")
        else:
            for i in range(len(arr) - 1, -1, -1):
                print(arr[i], end="")
                if i > 0:
                    print(",", end="")
        print("]")