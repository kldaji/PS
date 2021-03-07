moum = ['a','e','i','o','u']

def dfs(word, i):
  global L, C
  if len(word) == L:
    moum_cnt = 0
    jaum_cnt = 0
    for i in range(L):
      if word[i] in moum:
        moum_cnt += 1
      else:
        jaum_cnt += 1
    if moum_cnt >= 1 and jaum_cnt >= 2:
      print(word)
  else:
    for j in range(i, C):
      temp = word
      temp += alphas[j]
      dfs(temp, j+1)
      

L, C = map(int, input().split())
alphas = list(input().split())
alphas.sort()

dfs("", 0)

"""
dfs
back tracking
"""


from itertools import combinations

moum = ['a','e','i','o','u']

L, C = map(int, input().split())
alphas = list(input().split())
alphas.sort()

comb = combinations(alphas, L)

for c in comb:
  cnt = 0
  for letter in c:
    if letter in moum:
      cnt += 1
  if cnt >= 1 and (L-cnt) >= 2:
    print(''.join(c))

"""
Combination
(make code short)
"""
