import sys
input = sys.stdin.readline

n = int(input())
dpTable = [[0 for j in range(2)] for i in range(n + 1)]
dpTable[1][0] = 0
dpTable[1][1] = 1

for i in range(2, n + 1):
  dpTable[i][0] = dpTable[i - 1][0] + dpTable[i - 1][1]
  dpTable[i][1] = dpTable[i - 1][0]

print(dpTable[n][0] + dpTable[n][1])