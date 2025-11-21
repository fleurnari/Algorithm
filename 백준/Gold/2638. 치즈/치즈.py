import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
cheeseMap = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def bfs():
  visitList = [[False] * m for _ in range(n)]
  queue = deque()
  queue.append((0, 0))
  visitList[0][0] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visitList[nx][ny]:
          if cheeseMap[nx][ny] >= 1:
            cheeseMap[nx][ny] += 1
          else:
            visitList[nx][ny] = True
            queue.append((nx, ny))

def melt():
  tmp = 0
  for i in range(n):
    for j in range(m):
      if cheeseMap[i][j] >= 3:
        cheeseMap[i][j] = 0
        tmp += 1
      elif cheeseMap[i][j] >= 2:
        cheeseMap[i][j] = 1
  return tmp

while True:
  bfs()
  melted = melt()
  if melted:
    answer += 1
  else:
    print(answer)
    break