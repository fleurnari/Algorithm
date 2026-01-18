import sys
input = sys.stdin.readline
n = int(input())
mod = 10007
dpTable = [[0] * 53 for _ in range(53)]
dpTable[0][0] = dpTable[1][0] = dpTable[1][1] = 1
result = 0
cnt = 1
pos = 1

for i in range(2, 53):
  dpTable[i][0] = dpTable[i][i] = 1
  for j in range(1, i):
    dpTable[i][j] = dpTable[i - 1][j - 1] + dpTable[i - 1][j]

while n >= 4:
  result += pos * dpTable[13][cnt] * dpTable[52 - cnt * 4][n - 4]
  cnt += 1
  pos = -pos
  n -= 4

print(result % mod)