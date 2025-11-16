import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
up = -1
down = -1
answer = 0

for i in range(r):
  if a[i][0] == -1:
    up = i
    down = i + 1
    break

def spread():
  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]
  tmp = [[0] * c for _ in range(r)]
  for i in range(r):
    for j in range(c):
      if a[i][j] > 0:
        cnt = 0
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != -1:
            tmp[nx][ny] += a[i][j] // 5
            cnt += a[i][j] // 5
        a[i][j] -= cnt

  for i in range(r):
    for j in range(c):
      a[i][j] += tmp[i][j]

def cleanUp():
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0]
  direct = 0
  before = 0
  x, y = up, 1
  while True:
     nx = x + dx[direct]
     ny = y + dy[direct]
     if x == up and y == 0:
        break
     if nx < 0 or nx >= r or ny < 0 or ny >= c:
        direct += 1
        continue
     a[x][y], before = before, a[x][y]
     x, y = nx, ny

def cleanDown():
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  direct = 0
  before = 0
  x, y = down, 1
  while True:
    nx = x + dx[direct]
    ny = y + dy[direct]
    if x == down and y == 0:
        break
    if nx < 0 or nx >= r or ny < 0 or ny >= c:
        direct += 1
        continue
    a[x][y], before = before, a[x][y]
    x, y = nx, ny

for _ in range(t):
    spread()
    cleanUp()
    cleanDown()

for i in range(r):
  for j in range(c):
    if a[i][j] > 0:
       answer += a[i][j]

print(answer)