from sys import *

N = int(stdin.readline().rstrip())

office = {}

for _ in range(N):
    name, cmd = stdin.readline().rstrip().split()

    if cmd == "enter":
        office[name] = 1
    else:
        office.pop(name)

list_office = sorted(office, reverse=True)

print("\n".join(list_office))
