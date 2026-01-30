import sys
from collections import deque
input = sys.stdin.readline
m, n, k = map(int, input().split())
grid = [[0] * n for _ in range(m)]
for _ in range(k):
  a, b, c, d = map(int, input().split())
  for y in range(b, d):
    for x in range(a, c):
      grid[y][x] = 1
visitList = [[False] * n for _ in range(m)]
area = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visitList[x][y] = True
  a = 1
  while queue:
    qx, qy = queue.popleft()
    for i in range(4):
      nx, ny = qx + dx[i], qy + dy[i]
      if 0 <= nx < m and 0 <= ny < n:
        if not visitList[nx][ny] and grid[nx][ny] == 0:
          visitList[nx][ny] = True
          queue.append((nx, ny))
          a += 1
  return a

for i in range(m):
  for j in range(n):
    if grid[i][j] == 0 and not visitList[i][j]:
      area.append((bfs(i, j)))

area.sort()

print(len(area))
print(*area)