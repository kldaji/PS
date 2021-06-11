import sys

string = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())

s1 = list(string)
s2 = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "P":
        s1.append(cmd[1])
    elif cmd[0] == "L":
        if s1:
            s2.append(s1.pop())
    elif cmd[0] == "B":
        if s1:
            s1.pop()
    elif cmd[0] == "D":
        if s2:
            s1.append(s2.pop())

while len(s2) != 0:
    s1.append(s2.pop())

print("".join(s1))