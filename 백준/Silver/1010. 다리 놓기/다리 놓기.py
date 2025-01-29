import sys
input = sys.stdin.readline
dpTable = [[0 for j in range(31)] for i in range(31)]

for i in range(31):
  dpTable[i][1] = i
  dpTable[i][0] = 1
  dpTable[i][i] = 1

for i in range(2, 31):
  for j in range(1, i):
    dpTable[i][j] = dpTable[i - 1][j] + dpTable[i - 1][j - 1]

t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  print(dpTable[m][n])