import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
busData = [[sys.maxsize for j in range(n + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
  busData[i][i] = 0

for i in range(m):
  start, end, cost = map(int, input().split())
  if busData[start][end] > cost:
    busData[start][end] = cost

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if busData[i][j] > busData[i][k] + busData[k][j]:
        busData[i][j] = busData[i][k] + busData[k][j]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if busData[i][j] == sys.maxsize:
      print(0, end = ' ')
    else:
      print(busData[i][j], end = ' ')
  print()