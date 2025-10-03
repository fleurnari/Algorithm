import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visitList = [[[False] * m for _ in range(n)] for _ in range(h)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()
answer = 0

for i in range(h):
  for j in range(n):
    for k in range(m):
      if arr[i][j][k] == 1:
        queue.append((i, j, k))

def bfs():
  while queue:
    z, y, x = queue.popleft()
    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nz < h and 0 <= nx < m and 0 <= ny < n:
        if arr[nz][ny][nx] == 0 and not visitList[nz][ny][nx]:
          visitList[nz][ny][nx] = True
          arr[nz][ny][nx] = arr[z][y][x] + 1
          queue.append((nz, ny, nx))

bfs()

for i in arr:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
      else:
        answer = max(answer, max(j))

print(answer - 1)