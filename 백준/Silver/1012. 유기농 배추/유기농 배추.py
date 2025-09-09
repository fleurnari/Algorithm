import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(arr, x, y):
  queue = deque()
  queue.append([x, y])
  arr[x][y] = 0

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1:
        queue.append([nx, ny])
        arr[nx][ny] = 0

for _ in range(t):
  m, n, k = map(int, input().split())
  arr = [[0] * n for _ in range(m)]
  for _ in range(k):
    x, y = map(int, input().split())
    arr[x][y] = 1
  cnt = 0
  for j in range(m):
    for k in range(n):
      if arr[j][k] == 1:
        bfs(arr, j, k)
        cnt += 1

  print(cnt)