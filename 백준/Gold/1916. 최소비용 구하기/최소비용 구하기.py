import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distList = [sys.maxsize] * (n + 1)
visitList = [False] * (n + 1)

for _ in range(m):
  s, e, w = map(int, input().split())
  graph[s].append((e, w))

startIdx, endIdx = map(int, input().split())

def dkstra(start, end):
  pq = PriorityQueue()
  pq.put((0, start))
  distList[start] = 0
  while pq.qsize() > 0:
    currentNode = pq.get()
    current = currentNode[1]
    if not visitList[current]:
      visitList[current] = True
      for i in graph[current]:
        if not visitList[i[0]] and distList[i[0]] > distList[current] + i[1]:
          distList[i[0]] = distList[current] + i[1]
          pq.put((distList[i[0]], i[0]))

  return distList[end]

print(dkstra(startIdx, endIdx))   