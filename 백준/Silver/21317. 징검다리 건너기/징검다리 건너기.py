import sys
input = sys.stdin.readline
n = int(input())
smallJump = [0] * (n + 1)
bigJump = [0] * (n + 1)
for i in range(1, n):
  a, b = map(int, input().split())
  smallJump[i] = a
  bigJump[i] = b
k = int(input())
dpTable = [[sys.maxsize] * 2 for _ in range(n + 1)]
dpTable[1][0] = 0

for i in range(2, n + 1):
  dpTable[i][0] = min(dpTable[i][0], dpTable[i - 1][0] + smallJump[i - 1])
  dpTable[i][1] = min(dpTable[i][1], dpTable[i - 1][1] + smallJump[i - 1])
  if i >= 3:
    dpTable[i][0] = min(dpTable[i][0], dpTable[i - 2][0] + bigJump[i - 2])
    dpTable[i][1] = min(dpTable[i][1], dpTable[i - 2][1] + bigJump[i - 2])
  if i >= 4:
    dpTable[i][1] = min(dpTable[i][1], dpTable[i - 3][0] + k)

print(min(dpTable[n]))