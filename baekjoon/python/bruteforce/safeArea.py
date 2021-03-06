from copy import deepcopy

# 상 하 좌 우 변수
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(a,b, criteria):
  global height_temp
  # 기준 높이를 초과하는 영역의 큐
  q = []
  q.append([a,b])

  while q:
    x, y = q.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 상 하 좌 우를 모두 순회해서
      if nx >=0 and ny >=0 and nx < N and ny < N:
        # 기준 높이보다 높은 인접영역이 존재하면
        if height_temp[nx][ny] > criteria:
          # 큐에 넣어주고
          q.append([nx,ny])
          # 순회한 영역을 0으로 처리해서 중복된 접근을 막아준다.
          height_temp[nx][ny] = 0


N = int(input())

# 각 높이를 담을 수 있는 리스트
height = []
# 정답 변수
answer = 0

# N개의 row list를 입력받는다.
for i in range(N):
  height.append(list(map(int, input().split())))

# 높이 기준 0 ~ 99까지 전부 검사한다.
for i in range(100):
  # 기존 높이 정보 복사본을 할당한다.
  height_temp = deepcopy(height)
  # 영역 개수 변수
  temp = 0

  # 모든 높이 정보를 순회한다.
  for j in range(N):
    for k in range(N):
      # 물에 잠기지 않는다면
      if height_temp[j][k] > i:
        # 중복 접근을 막아주고
        height_temp[j][k] = 0
        # bfs로 물에 잠기지 않는 인접 영역들을 처리한다.
        bfs(j,k,i)
        # 인접 영역을 처리하고 영역 개수를 1 증가시킨다.
        temp += 1
  # i 높이 기준에 따른 영역과 정답 변수 중 최대값을 구해준다.
  answer = max(answer, temp)

# 정답을 출력한다.
print(answer)

"""
bfs
"""
