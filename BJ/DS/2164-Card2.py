import sys
import collections

n = int(sys.stdin.readline().rstrip())

deque = collections.deque([i for i in range(1, n + 1)])

while len(deque) > 1:
    deque.popleft()
    deque.rotate(-1)  # Move Left

print(deque[0])


"""
<TIME OUT>
q = []

for i in range(n, 0, -1):
    q.append(i)

while len(q) != 1:
    q.pop()
    top = q.pop()
    q.insert(0, top)

print(q[0])
"""