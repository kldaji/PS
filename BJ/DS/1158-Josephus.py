import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

queue = []

for i in range(n):
    queue.append(str(i + 1))

result = []
pos = 0

while len(queue) != 0:
    pos = (pos + k - 1) % len(queue)
    result.append(queue.pop(pos))

print("<%s>" % (", ".join(result)))
