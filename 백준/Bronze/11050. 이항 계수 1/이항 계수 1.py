import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dpTable = [[0 for j in range(n + 1)] for i in range(n + 1)]

for i in range(n + 1):
  dpTable[i][0] = 1
  dpTable[i][1] = i
  dpTable[i][i] = 1

for i in range(2, n + 1):
  for j in range(1, i):
    dpTable[i][j] = dpTable[i - 1][j - 1] + dpTable[i - 1][j]

print(dpTable[n][k])