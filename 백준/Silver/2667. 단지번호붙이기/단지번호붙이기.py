import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
  arr.append(list(map(int, input().rstrip())))

def bfs(arr, x, y):
  queue = deque()
  queue.append((x, y))
  arr[x][y] = 0
  cnt = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if arr[nx][ny] == 1:
        arr[nx][ny] = 0
        queue.append((nx, ny))
        cnt += 1
  return cnt

arr2 = [bfs(arr, i, j) for i in range(n) for j in range(n) if arr[i][j] == 1]
arr2.sort()
print(len(arr2))

for i in range(len(arr2)):
  print(arr2[i])