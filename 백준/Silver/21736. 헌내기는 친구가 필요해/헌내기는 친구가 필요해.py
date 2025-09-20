import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
campus = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visitList = [[False] * m for _ in range(n)]
result = 0
x, y = 0, 0

for i in range(n):
  campus.append(list(input().rstrip()))
  for j in range(m):
    if campus[i][j] == 'I':
      x, y = i, j

queue = deque()
queue.append([x, y])

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and visitList[nx][ny] == False:
      visitList[nx][ny] = True
      if campus[nx][ny] == 'O':
        queue.append([nx, ny])
      elif campus[nx][ny] == 'P':
        queue.append([nx, ny])
        result += 1

if result == 0:
  print('TT')
else:
  print(result)