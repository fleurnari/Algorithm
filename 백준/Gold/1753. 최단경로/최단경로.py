import sys
input = sys.stdin.readline
from queue import PriorityQueue

v, e = map(int, input().split())
k = int(input())
routeList = [[] for i in range(v + 1)]
distList = [sys.maxsize] * (v + 1)
visited = [False] * (v + 1)
queue = PriorityQueue()

for i in range(e):
  s, e, w = map(int, input().split())
  routeList[s].append((e, w))

queue.put((0, k))
distList[k] = 0

while queue.qsize() > 0:
  now = queue.get()
  node = now[1]
  if visited[node]:
    continue
  visited[node] = True 
  for i in routeList[node]:
    target = i[0]
    weight = i[1]
    if distList[target] > distList[node] + weight:
      distList[target] = distList[node] + weight
      queue.put((distList[target], target))

for i in range(1, v + 1):
  if visited[i]:
    print(distList[i])
  else:
    print("INF")