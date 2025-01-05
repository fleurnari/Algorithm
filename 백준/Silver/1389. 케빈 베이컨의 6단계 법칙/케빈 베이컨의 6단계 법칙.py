import sys
n, m = map(int, input().split())
connectData = [[sys.maxsize for j in range(n + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
  connectData[i][i] = 0

for i in range(m):
  start, end = map(int, input().split())
  connectData[start][end] = 1
  connectData[end][start] = 1

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if connectData[i][j] > connectData[i][k] + connectData[k][j]:
        connectData[i][j] = connectData[i][k] + connectData[k][j]

minCnt = sys.maxsize
answer = -1

for i in range(1, n + 1):
  tmp = 0
  for j in range(1, n + 1):
    tmp += connectData[i][j]
  if minCnt > tmp:
    minCnt = tmp
    answer = i

print(answer)