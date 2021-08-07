from sys import *
from collections import deque

N, M = map(int, stdin.readline().rstrip().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

maze = []

# Get Maze Info
for _ in range(N):
    maze.append(list(stdin.readline().rstrip()))

queue = deque()

# start coordinate
queue.append((0, 0))

# "1" -> 1
maze[0][0] = 1

# Loop until empty
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # In-Range
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == "1":
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

# (N, M)
print(maze[N-1][M-1])
