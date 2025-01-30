import sys
input = sys.stdin.readline
n = int(input())
dpTable = [0] * (n + 1)
dpTable[1] = 0

for i in range(2, n + 1):
  dpTable[i] = dpTable[i - 1] + 1
  if i % 2 == 0:
    dpTable[i] = min(dpTable[i], dpTable[i // 2] + 1)
  if i % 3 == 0:
    dpTable[i] = min(dpTable[i], dpTable[i // 3] + 1)

print(dpTable[n])