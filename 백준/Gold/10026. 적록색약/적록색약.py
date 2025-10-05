import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [list(input()) for _ in range(n)]
visitList = [[False] * n for _ in range(n)]
answer = [0, 0]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visitList[x][y] = True

  while queue:
    x, y = queue.popleft()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if arr[x][y] == arr[nx][ny] and not visitList[nx][ny]:
          visitList[nx][ny] = True
          queue.append((nx, ny))


for i in range(n):
  for j in range(n):
    if not visitList[i][j]:
      bfs(i, j)
      answer[0] += 1

for i in range(n):
  for j in range(n):
    if arr[i][j] == 'G':
      arr[i][j] = 'R'

visitList = [[False] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if not visitList[i][j]:
      bfs(i, j)
      answer[1] += 1

print(*answer)