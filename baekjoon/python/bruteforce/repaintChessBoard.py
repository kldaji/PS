# maxsize
import sys 

# get N(세로) and M(가로)
N, M = map(int, input().split())

chess_board = []

# get chess board information
for i in range(N):
  temp = list(input())
  chess_board.append(temp)

# check board view
# print(chess_board)

# 0 ~ N-8 범위 check (가로)
# 0 ~ M-8 범위 check (세로)
# 반복문 -> row기준으로 column을 하나씩 check

# init intMAX
ans = sys.maxsize
# test for maxsize
# print(ans)

# +1해주는 이유는 N-8을 포함시켜주기 위해서
for i in range(0, N-8+1):
  for j in range(0, M-8+1):
    temp = 0
    for k in range(i, i+8):
      if k % 2 == 0:
        for l in range(j, j+8):
          # case 1
          if l % 2 == 0:
            if chess_board[k][l] != 'W':
              temp += 1
          else:
            if chess_board[k][l] != 'B':
              temp += 1
      else:
        for l in range(j, j+8):
          # case 1
          if l % 2 == 0:
            if chess_board[k][l] != 'B':
              temp += 1
          else:
            if chess_board[k][l] != 'W':
              temp += 1

    ans = min(ans, temp)

    temp = 0
    for k in range(i, i+8):
      if k % 2 == 0:
        for l in range(j, j+8):
          # case 2
          if l % 2 == 0:
            if chess_board[k][l] != 'B':
              temp += 1
          else:
            if chess_board[k][l] != 'W':
              temp += 1
      else:
        for l in range(j, j+8):
          # case 2
          if l % 2 == 0:
            if chess_board[k][l] != 'W':
              temp += 1
          else:
            if chess_board[k][l] != 'B':
              temp += 1

    ans = min(ans, temp)

print(ans)

"""
Too Hard to read code -> need to organize
"""        
 



"""
<Organized Version>
"""
# maxsize
import sys 

# get N(세로) and M(가로)
N, M = map(int, input().split())

chess_board = []

# get chess board information
for i in range(N):
  temp = list(input())
  chess_board.append(temp)

# check board view
# print(chess_board)

# 0 ~ N-8 범위 check (가로)
# 0 ~ M-8 범위 check (세로)
# 반복문 -> row기준으로 column을 하나씩 check

# init intMAX
ans = sys.maxsize
# test for maxsize
# print(ans)

# +1해주는 이유는 N-8을 포함시켜주기 위해서
for i in range(0, N-8+1):
  for j in range(0, M-8+1):
    start_W = 0
    start_B = 0
    for k in range(i, i+8):
      for l in range(j, j+8):
        if (k+l) % 2 == 0:
          if chess_board[k][l] != 'W':
            start_W += 1
          if chess_board[k][l] != 'B':
            start_B += 1
        else:
          if chess_board[k][l] != 'B':
            start_W += 1
          if chess_board[k][l] != 'W':
            start_B += 1

    ans = min(start_W, start_B, ans)

print(ans)

        
 

