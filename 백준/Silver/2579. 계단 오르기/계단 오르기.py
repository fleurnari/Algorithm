import sys
input = sys.stdin.readline
n = int(input())
stair = [0] * 301
dpTable = [0] * 301

for i in range(n):
  stair[i] = int(input())

dpTable[0] = stair[0]
dpTable[1] = stair[0] + stair[1]
dpTable[2] = max(stair[1] + stair[2], stair[0] + stair[2])

for i in range(3, n):
  dpTable[i] = max(dpTable[i - 3] + stair[i - 1] + stair[i], dpTable[i - 2] + stair[i])

print(dpTable[n - 1])