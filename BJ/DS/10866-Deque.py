import sys

n = int(sys.stdin.readline().rstrip())

deque = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip().split(" ")

    if cmd[0] == "push_back":
        deque.insert(0, int(cmd[1]))
    elif cmd[0] == "push_front":
        deque.append(int(cmd[1]))
    elif cmd[0] == "front":
        if deque:
            print(deque[-1])
        else:
            print(-1)
    elif cmd[0] == "back":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif cmd[0] == "pop_front":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)