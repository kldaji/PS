import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_name = {}
pokemon_num = {}

for i in range(1, n + 1):
    name = input().strip()
    pokemon_name[name] = i
    pokemon_num[str(i)] = name

for _ in range(m):
    cmd = input().strip()
    if cmd.isdigit():
        print(pokemon_num[cmd])
    else:
        print(pokemon_name[cmd])