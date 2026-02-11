import sys
input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())
block = set()
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1

for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  block.add((x1, y1, x2, y2))
  block.add((x2, y2, x1, y1))

for i in range(n + 1):
  for j in range(m + 1):
    if i > 0 and (i - 1, j, i, j) not in block:
      dp[i][j] += dp[i - 1][j]
    if j > 0 and (i, j - 1, i, j) not in block:
      dp[i][j] += dp[i][j - 1]

print(dp[n][m])