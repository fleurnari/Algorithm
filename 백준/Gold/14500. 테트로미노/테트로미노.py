import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visitList = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maxValue = max(map(max, arr))
answer = 0

def dfs(x, y, tmp, cur):
  global answer

  if answer >= cur + maxValue * (4 - tmp):
    return
  
  if tmp == 4:
    answer = max(answer, cur)
    return

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and not visitList[nx][ny]:
      if tmp == 2:
        visitList[nx][ny] = True
        dfs(x, y, tmp + 1, cur + arr[nx][ny])
        visitList[nx][ny] = False
      visitList[nx][ny] = True
      dfs(nx, ny, tmp + 1, cur + arr[nx][ny])
      visitList[nx][ny] = False

for i in range(n):
  for j in range(m):
    visitList[i][j] = True
    dfs(i, j, 1, arr[i][j])
    visitList[i][j] = False

print(answer)