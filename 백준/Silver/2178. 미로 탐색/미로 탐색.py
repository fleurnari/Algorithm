from collections import deque

xArr = [0, 1, 0, -1]
yArr = [1, 0, -1, 0]

n, m = map(int, input().split())

arr = [[0] * m for i in range(n)]

visitList = [[0] * m for i in range(n)]

for i in range(n):
  num = list(input())
  for j in range(m):
    arr[i][j] = int(num[j])

def bfs(a, b):
  q = deque()
  q.append((a, b))
  visitList[a][b] = True

  while q:
    now = q.popleft()
    
    for i in range(4):
      x = now[0] + xArr[i]
      y = now[1] + yArr[i]

      if x >= 0 and y >= 0 and x < n and y < m:
        if not visitList[x][y] and arr[x][y] != 0:
          visitList[x][y] = True
          arr[x][y] = arr[now[0]][now[1]] + 1
          q.append((x, y))

bfs(0, 0)
print(arr[n - 1][m - 1])