import sys
from collections import deque
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def bfs():
  global answer
  queue = deque()
  tmpMap = copy.deepcopy(map)

  for i in range(n):
    for j in range(m):
      if tmpMap[i][j] == 2:
        queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and tmpMap[nx][ny] == 0:
        tmpMap[nx][ny] = 2
        queue.append((nx, ny))

  cnt = 0
  for i in range(n):
    cnt += tmpMap[i].count(0)
  answer = max(answer, cnt)

def makeWall(cnt):
  if cnt == 3:
    bfs()
    return

  for i in range(n):
    for j in range(m):
      if map[i][j] == 0:
        map[i][j] = 1
        makeWall(cnt + 1)
        map[i][j] = 0

makeWall(0)
print(answer)