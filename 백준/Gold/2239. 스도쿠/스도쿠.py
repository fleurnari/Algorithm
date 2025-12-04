import sys
input = sys.stdin.readline

sdoku = [list(map(int, input().rstrip())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if sdoku[i][j] == 0]
isFinish = False

def chkValid(x, y, num):
  for i in range(9):
    if sdoku[x][i] == num:
      return False

  for i in range(9):
    if sdoku[i][y] == num:
      return False

  nx = (x // 3) * 3
  ny = (y // 3) * 3
  for i in range(3):
    for j in range(3):
      if sdoku[nx + i][ny + j] == num:
        return False
  return True

def dfs(depth):
  global isFinish
  if isFinish:
    return

  if depth == len(zero):
    for row in sdoku:
      print("".join(map(str, row)))
    isFinish = True
    return

  x, y = zero[depth]
  for num in range(1, 10):
    if chkValid(x, y, num):
      sdoku[x][y] = num
      dfs(depth + 1)
      sdoku[x][y] = 0

dfs(0)
