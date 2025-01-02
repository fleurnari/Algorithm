import sys
input = sys.stdin.readline
n, startCity, endCity, m = map(int, input().split())
edgeList = []
distList = [-sys.maxsize] * n

for i in range(m):
  start, end, cost = map(int, input().split())
  edgeList.append((start, end, cost))

cityMoney = list(map(int, input().split()))

distList[startCity] = cityMoney[startCity]

for i in range(n + 101):
  for start, end, cost in edgeList:
    if distList[start] == -sys.maxsize:
      continue
    elif distList[start] == sys.maxsize:
      distList[end] = sys.maxsize
    elif distList[end] < distList[start] + cityMoney[end] - cost:
      distList[end] = distList[start] + cityMoney[end] - cost
      if i >= n - 1:
        distList[end] = sys.maxsize

if distList[endCity] == -sys.maxsize:
  print("gg")
elif distList[endCity] == sys.maxsize:
  print("Gee")
else:
  print(distList[endCity])