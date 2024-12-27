import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edgeList = []
timeList = [sys.maxsize] * (n + 1)

for i in range(m):
  start, end, time = map(int, input().split())
  edgeList.append((start, end, time))

timeList[1] = 0

for i in range(n - 1):
  for start, end, time in edgeList:
    if timeList[start] != sys.maxsize and timeList[end] > timeList[start] + time:
      timeList[end] = timeList[start] + time

minusCycle = False

for start, end, time in edgeList:
  if timeList[start] != sys.maxsize and timeList[end] > timeList[start] + time:
    minusCycle = True

if minusCycle:
  print(-1)
else:
  for i in range(2, n + 1):
    if timeList[i] != sys.maxsize:
      print(timeList[i])
    else:
      print(-1)

