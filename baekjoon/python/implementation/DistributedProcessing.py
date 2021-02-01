tc = int(input())

s = [[], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]

for _ in range(tc):
  a, b = map(int, input().split())
  a = a % 10
  if a != 0:
    print(s[a][b % len(s[a])])
  else:
    print(10)

"""
반복 제곱수!!!
"""
