import sys
input = sys.stdin.readline

n = int(input())
dpTable = [[0 for j in range(11)] for i in range(n + 1)]
result = 0
mod = 1000000000

for i in range(1, 10):
  dpTable[1][i] = 1

for i in range(2, n + 1):
  dpTable[i][0] = dpTable[i - 1][1]
  dpTable[i][9] = dpTable[i - 1][8]
  for j in range(1, 9):
    dpTable[i][j] = dpTable[i - 1][j - 1] + dpTable[i - 1][j + 1]

for i in range(10):
  result = (result + dpTable[n][i]) % mod

print(result)