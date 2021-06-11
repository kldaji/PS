import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

deq = deque([i for i in range(1, n + 1)])

seq = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0

for s in seq:
    front = deq[0]
    rear = deq[-1]

    if front == s:
        deq.popleft()
    else:
        pos = deq.index(s)
        if pos < len(deq) / 2:
            while s != deq[0]:
                deq.rotate(-1)
                cnt += 1
            deq.popleft()
        else:
            while s != deq[0]:
                deq.rotate(1)
                cnt += 1
            deq.popleft()

print(cnt)