import sys
input = sys.stdin.readline
dpTable = [[0 for j in range(15)] for i in range(15)]

for i in range(1, 15):
  dpTable[i][1] = 1
  dpTable[0][i] = i

for i in range(1, 15):
  for j in range(2, 15):
    dpTable[i][j] = dpTable[i][j - 1] + dpTable[i - 1][j]

t = int(input())

for i in range(t):
  k = int(input())
  n = int(input())
  print(dpTable[k][n])