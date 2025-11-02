import sys
from queue import PriorityQueue
input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
dist = [sys.maxsize] * (v + 1)
visitList = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
queue = PriorityQueue()

for _ in range(e):
  s, e, w = map(int, input().split())
  graph[s].append((e, w))

queue.put((0, k))
dist[k] = 0

while queue.qsize() > 0:
  current = queue.get()
  currentV = current[1]
  if visitList[currentV]:
    continue
  visitList[currentV] = True
  for tmp in graph[currentV]:
    next = tmp[0]
    value = tmp[1]
    if dist[next] > dist[currentV] + value:
      dist[next] = dist[currentV] + value
      queue.put((dist[next], next))

for i in range(1, v + 1):
  if visitList[i]:
    print(dist[i])
  else:
    print("INF")