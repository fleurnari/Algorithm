import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
dpTable = [[0 for j in range(202)] for i in range(202)]

for i in range(201):
  for j in range(i + 1):
    if j == 0 or j == i:
      dpTable[i][j] = 1
    else:
      dpTable[i][j] = dpTable[i - 1][j - 1] + dpTable[i - 1][j]
      if dpTable[i][j] > 1000000000:
        dpTable[i][j] = 1000000001

if dpTable[n + m][m] < k:
  print(-1)
else:
  while not (n == 0 and m == 0):
    if dpTable[n - 1 + m][m] >= k:
      print("a", end = '')
      n -= 1
    else:
      print("z", end = '')
      k -= dpTable[n - 1 + m][m]
      m -= 1