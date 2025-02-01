import sys
input = sys.stdin.readline
dpTable = [[0 for j in range(1001)] for i in range(1001)]
n, m = map(int, input().split())
tmp = 0

for i in range(n):
  inputList = list(input())
  for j in range(m):
    dpTable[i][j] = int(inputList[j])
    if dpTable[i][j] == 1 and i > 0 and j > 0:
      dpTable[i][j] = min(dpTable[i - 1][j], dpTable[i][j - 1], dpTable[i - 1][j - 1]) + 1
    if dpTable[i][j] > tmp:
      tmp = dpTable[i][j]

print(tmp * tmp)