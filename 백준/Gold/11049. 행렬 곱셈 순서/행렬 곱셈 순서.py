import sys
input = sys.stdin.readline
n = int(input())
matrix = []
dpTable = [[-1 for j in range(n + 1)] for i in range(n + 1)]

matrix.append((0, 0))

for _ in range(n):
  r, c = map(int, input().split())
  matrix.append((r, c))

def calculate(x, y):
  result = sys.maxsize
  if dpTable[x][y] != -1:
    return dpTable[x][y]
  if x == y:
    return 0
  if x + 1 == y:
    return matrix[x][0] * matrix[x][1] * matrix[y][1]
  for i in range(x, y):
    result = min(result, matrix[x][0] * matrix[i][1] * matrix[y][1] + calculate(x, i) + calculate(i + 1, y))
  dpTable[x][y] = result
  return dpTable[x][y]

print(calculate(1, n))