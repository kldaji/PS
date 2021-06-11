import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

person = {}

for i in range(n):
    name = sys.stdin.readline().rstrip()
    person[name] = 1

for i in range(m):
    name = sys.stdin.readline().rstrip()
    if name in person:
        person[name] += 1
    else:
        person[name] = 1

person_list = []

for key, value in person.items():
    if value == 2:
        person_list.append(key)

person_list.sort()

print(len(person_list))
for pl in person_list:
    print(pl)