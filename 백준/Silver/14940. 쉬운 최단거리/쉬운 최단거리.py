import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0 for j in range(m)] for i in range(n)]
visitList = [[-1 for j in range(m)] for i in range(n)]

for i in range(n):
  arr[i] = list(map(int, input().split()))

for i in range(n):
  for j in range(m):
    if arr[i][j] == 2:
      start = (i, j)
    elif arr[i][j] == 0:
      visitList[i][j] = 0

def bfs(arr, visitList, start):
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  queue = deque([start])
  visitList[start[0]][start[1]] = 0
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visitList[nx][ny] == -1 and arr[nx][ny] == 1:
        visitList[nx][ny] = visitList[x][y] + 1
        queue.append((nx, ny))

bfs(arr, visitList, start)

for i in range(n):
  for j in range(m):
    print(visitList[i][j], end = ' ')
  print()