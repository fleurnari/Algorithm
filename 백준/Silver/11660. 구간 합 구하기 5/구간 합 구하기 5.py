import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

dpTable = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    dpTable[i][j] = dpTable[i][j - 1] + dpTable[i - 1][j] - dpTable[i - 1][j - 1] + arr[i - 1][j - 1]

for i in range(m):
  x1, y1, x2, y2 = map(int, input().split())

  print(dpTable[x2][y2] - dpTable[x2][y1 - 1] - dpTable[x1 - 1][y2] + dpTable[x1 - 1][y1 - 1])