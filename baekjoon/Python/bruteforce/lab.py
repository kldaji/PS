from copy import deepcopy

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def spreadVirus(lab_copy):
  global virus, dx, dy, answer
  virus_copy = deepcopy(virus)
  while virus_copy:
    x, y = virus_copy.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and ny >= 0 and nx < N and ny < M:
        if lab_copy[nx][ny] == 0:
          lab_copy[nx][ny] = 2
          virus_copy.append([nx,ny])
    
  cnt_temp = 0
  for i in range(N):
    for j in range(M):
      if lab_copy[i][j] == 0:
        cnt_temp += 1
  answer = max(answer, cnt_temp)

def makeWall(cnt, lab):
  lab_copy = deepcopy(lab)
  if cnt == 3:
    spreadVirus(lab_copy)
  else:
    for i in range(N):
      for j in range(M):
        if lab_copy[i][j] == 0:
          lab_copy[i][j] = 1
          makeWall(cnt+1, lab_copy)
          lab_copy[i][j] = 0


# 지도의 크기
N, M = map(int, input().split())

lab = []
virus = []
answer = 0

for i in range(N):
  lab.append(list(map(int, input().split())))
  for j in range(M):
    if lab[i][j] == 2:
      virus.append([i,j])

makeWall(0, lab)
    
print(answer)

"""
BFS
Recursion
Implementation
"""
