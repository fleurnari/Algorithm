import sys
input = sys.stdin.readline
n = int(input())
dpTable = [0] * (n + 2)
timeTable = [0] * (n + 1)
priceTable = [0] * (n + 1)

for i in range(1, n + 1):
  timeTable[i], priceTable[i] = map(int, input().split())

for i in range(n, 0, -1):
  if i + timeTable[i] > n + 1:
    dpTable[i] = dpTable[i + 1]
  else:
    dpTable[i] = max(dpTable[i + 1], dpTable[i + timeTable[i]] + priceTable[i])

print(dpTable[1])