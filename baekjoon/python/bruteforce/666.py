N = int(input())

cnt = 0

for i in range(666, 3000000):
  temp_cnt = 0
  temp = i
  while temp > 0:
    if temp % 10 == 6:
      temp_cnt += 1
    else:
      temp_cnt = 0
    if temp_cnt >= 3:
      cnt += 1
      break
    temp //= 10
  if cnt == N:
    print(i)
    break

"""
My own Version
-> too complicate
"""

N = int(input())

cnt = 0
num = 666
while True:
  if '666' in str(num):
    cnt += 1
  if cnt == N:
    print(num)
    break
  num += 1

"""
refer to google
much eaiser to understand
"""
