n = int(input())
routeData = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
  routeData[i] = list(map(int, input().split()))

for k in range(n):
  for i in range(n):
    for j in range(n):
      if routeData[i][k] == 1 and routeData[k][j] == 1:
        routeData[i][j] = 1

for i in range(n):
  for j in range(n):
    print(routeData[i][j], end = ' ')
  print()