# 유사 회문
def pseudo(word, s, e):
  while s < e:
    if word[s] == word[e]:
      s += 1
      e -= 1
    else:
      return False
  return True

# 회문
def palindrome(word, s, e):
  while s < e:
    if word[s] == word[e]:
      s += 1
      e -= 1
    else:
      r1 = pseudo(word, s+1, e)
      r2 = pseudo(word, s, e-1)
      if r1 or r2:
        return 1
      else:
        return 2
  return 0
  

T = int(input())

for _ in range(T):
  word = input()
  s = 0
  e = len(word) - 1

  print(palindrome(word, s, e))
  

"""
Try to use function 
"""
