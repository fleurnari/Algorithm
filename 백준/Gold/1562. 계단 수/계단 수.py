import sys
input = sys.stdin.readline
n = int(input())
numRange = 10
bitRange = 1 << numRange
dpTable = [[[0] * (bitRange) for _ in range(numRange)] for _ in range(n + 1)]
mod = 1000000000
answer = 0

for i in range(numRange):
  dpTable[1][i][1 << i] = 1

for i in range(1, n):
  for j in range(numRange):
    for k in range(bitRange):
      if 0 <= j < 9:
        tmp = k | 1 << (j + 1)
        dpTable[i + 1][j + 1][tmp] += dpTable[i][j][k]
        dpTable[i + 1][j + 1][tmp] %= mod
      if 0 < j <= 9:
        tmp = k | 1 << (j - 1)
        dpTable[i + 1][j - 1][tmp] += dpTable[i][j][k]
        dpTable[i + 1][j - 1][tmp] %= mod

for i in range(1, numRange):
  answer += dpTable[n][i][0b1111111111]
  answer %= mod

print(answer)