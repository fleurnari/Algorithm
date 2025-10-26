import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dpTable = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
  w, v = map(int, input().split())
  for j in range(1, k + 1):
    if j < w:
      dpTable[i][j] = dpTable[i - 1][j]
    else:
      dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i - 1][j - w] + v)

print(dpTable[n][k])