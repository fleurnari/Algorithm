import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  dpTable = [list(map(int, input().split())) for _ in range(2)]

  if n == 1:
    print(max(dpTable[0][0], dpTable[1][0]))
    continue
  
  dpTable[0][1] += dpTable[1][0]
  dpTable[1][1] += dpTable[0][0]

  if n == 2:
    print(max(dpTable[0][1], dpTable[1][1]))
    continue
  
  for i in range(2, n):
    dpTable[0][i] += max(dpTable[1][i - 1], dpTable[1][i - 2])
    dpTable[1][i] += max(dpTable[0][i - 1], dpTable[0][i - 2])

  print(max(dpTable[0][n - 1], dpTable[1][n - 1]))