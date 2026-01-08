import sys
input = sys.stdin.readline
n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
visitList = [[False] * (n * 3) for _ in range(2)]

def dfs(x, y, cnt):
  global answer
  if n % 2:
    if y == n:
      x += 1
      y = 0
    elif y == n + 1:
      x += 1
      y = 1
  else:
    if y == n:
      x += 1
      y = 1
    elif y == n + 1:
      x += 1
      y = 0

  if x == n:
    if answer < cnt:
      answer = cnt
    return
  if chess[x][y] == 1 and not visitList[0][x + y] and not visitList[1][x - y]:
    visitList[0][x + y] = True
    visitList[1][x - y] = True
    dfs(x, y + 2, cnt + 1)
    visitList[0][x + y] = False
    visitList[1][x - y] = False

  dfs(x, y + 2, cnt)

answer = 0
dfs(0, 0, 0)
black = answer
answer = 0
dfs(0, 1, 0)
white = answer

print(black + white)