import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
position = []
cnt = 0

for i in range(n):
  for j in range(n):
    if map[i][j] == 9:
      position.append(i)
      position.append(j)

def bfs(x, y):
  visitList = [[0] * n for _ in range(n)]
  queue = deque([[x, y]])
  visitList[x][y] = 1
  candidate = []

  while queue:
    i, j = queue.popleft()
    for idx in range(4):
      nx = i + dx[idx]
      ny = j + dy[idx]
      if 0 <= nx < n and 0 <= ny < n and visitList[nx][ny] == 0:
        if map[nx][ny] < map[x][y] and map[nx][ny] != 0:
          visitList[nx][ny] = visitList[i][j] + 1
          candidate.append((visitList[nx][ny] - 1, nx, ny))
        elif map[nx][ny] == map[x][y] or map[nx][ny] == 0:
          visitList[nx][ny] = visitList[i][j] + 1
          queue.append([nx, ny])

  return sorted(candidate, key = lambda x: (x[0], x[1], x[2]))

i, j = position
size = [2, 0]
while True:
  map[i][j] = size[0]
  candidate = deque(bfs(i, j))

  if not candidate:
    break

  step, x, y = candidate.popleft()
  cnt += step
  size[1] += 1
  if size[0] == size[1]:
    size[0] += 1
    size[1] = 0

  map[i][j] = 0
  i, j = x, y

print(cnt)