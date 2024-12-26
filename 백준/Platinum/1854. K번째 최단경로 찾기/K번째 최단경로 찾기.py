import sys
import heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())
routeList = [[] for i in range(n + 1)]
timeList = [[sys.maxsize] * k for i in range(n + 1)]

for i in range(m):
  a, b, c = map(int, input().split())
  routeList[a].append([b, c])

pq = [(0, 1)]
timeList[1][0] = 0

while pq:
  time, node = heapq.heappop(pq)
  for nNode, nTime in routeList[node]:
    newTime = time + nTime
    if timeList[nNode][k - 1] > newTime:
      timeList[nNode][k - 1] = newTime
      timeList[nNode].sort()
      heapq.heappush(pq, (newTime, nNode))

for i in range(1, n + 1):
  if timeList[i][k - 1] == sys.maxsize:
    print(-1)
  else:
    print(timeList[i][k - 1])