import sys
input = sys.stdin.readline
t = int(input())
dpTable = [[0 for j in range(15)] for i in range(15)]

for i in range(15):
  dpTable[0][i] = i

for i in range(1, 15):
  for j in range(1, 15):
    dpTable[i][j] = dpTable[i - 1][j] + dpTable[i][j - 1]

for i in range(t):
  k = int(input())
  n = int(input())
  print(dpTable[k][n])