import statistics
from collections import Counter

N = int(input())

nums = []
for _ in range(N):
  temp = int(input())
  nums.append(temp)
nums.sort()

print(round(sum(nums)/N))
print(statistics.median(nums))

cnt = Counter(nums)
if len(nums) != 1:  
  temp = cnt.most_common(2)
  if temp[0][1] == temp[1][1]:
    print(temp[1][0])
  else:
    print(temp[0][0])
else:
  temp = cnt.most_common(1)
  print(temp[0][0])

print(max(nums) - min(nums))

"""
<median>
- import statistic
- statistic.median()

<frequency>
- from collections import Counter
- Counter()
- most_common

<round>
- / vs //
- round()

"""
