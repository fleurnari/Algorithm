import sys

input = sys.stdin.readline

n, m = map(int, input().split())

orgArr = [[0] * (n + 1)]

sumArr = [[0] * (n + 1) for i in range(n + 1)]


for i in range(n):
  orgRow = [0] + [int(x) for x in input().split()]
  orgArr.append(orgRow)

for i in range(1, n + 1):
  for j in range(1, n + 1):
      sumArr[i][j] = sumArr[i][j - 1] + sumArr[i - 1][j] - sumArr[i - 1][j - 1] + orgArr[i][j]


for i in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(sumArr[x2][y2] - sumArr[x1 - 1][y2] - sumArr[x2][y1 - 1] + sumArr[x1 - 1][y1 - 1])