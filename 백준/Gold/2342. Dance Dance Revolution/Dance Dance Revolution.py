import sys
input = sys.stdin.readline
arr = list(map(int, input().split()))
dpTable = [[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]
move = [[0, 2, 2, 2, 2],
             [2, 1, 3, 4, 3],
             [2, 3, 1, 3, 4],
             [2, 4, 3, 1, 3],
             [2, 3, 4, 3, 1]]
dpTable[0][0][0] = 0
idx = 0
s = 1
result = sys.maxsize

while arr[idx] != 0:
  n = arr[idx]
  for i in range(5):
    if n == i:
      continue
    for j in range(5):
      dpTable[s][i][n] = min(dpTable[s - 1][i][j] + move[j][n], dpTable[s][i][n])

  for j in range(5):
    if n == j:
      continue
    for i in range(5):
      dpTable[s][n][j] = min(dpTable[s - 1][i][j] + move[i][n], dpTable[s][n][j])

  s += 1
  idx += 1

s -= 1

for i in range(5):
  for j in range(5):
    result = min(result, dpTable[s][i][j])

print(result)