import sys
input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(m)]
visitList = [[False] * n for _ in range(m)]
visitList[0][0] = True

for i in range(m):
  for j in range(n):
    if city[i][j] == 0:
      continue
    if i > 0 and visitList[i - 1][j]:
      visitList[i][j] = True
    if j > 0 and visitList[i][j - 1]:
      visitList[i][j] = True

print("Yes" if visitList[m - 1][n - 1] else "No")