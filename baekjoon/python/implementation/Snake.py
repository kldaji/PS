from collections import deque

N = int(input())
K = int(input())

board = []
for i in range(N):
  board.append([0]*N)

for i in range(K):
  x, y = map(int, input().split())
  board[x-1][y-1] = 1

L = int(input())
rotate = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(L):
  t, direct = input().split()
  t = int(t)
  rotate.append([t, direct])

curX = 0
curY = 0
direction = 0

snake = deque()
snake.append([curX,curY])
ansTime = 0
rotate_idx = 0

while True:
  if rotate_idx < L and ansTime == rotate[rotate_idx][0]:
    if rotate[rotate_idx][1] == 'D':
      direction += 1
      direction %= 4
    else:
      direction += 3
      direction %= 4
    rotate_idx += 1
  
  curX += dx[direction]
  curY += dy[direction]
  if 0 <= curX <N and 0 <= curY < N:   
    if [curX,curY] in snake:
      break
    if board[curX][curY] == 0:
      snake.popleft()
    else:
      board[curX][curY] = 0
    snake.append([curX,curY])
    ansTime += 1
  else:
    break

print(ansTime+1)

"""
<deque>
from collections import deque
- append, appendleft
- pop, popleft


"""
