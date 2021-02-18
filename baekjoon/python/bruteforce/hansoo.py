N = int(input())

if N < 100:
  print(N)
else:
  ans = 99
  for i in range(100, N+1):
    # int to list
    nums = list(map(int, str(i)))
    if nums[0] - nums[1] == nums[1] - nums[2]:
      ans += 1
  print(ans)

"""
int -> list
"""
