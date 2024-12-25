import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
m = int(input())
busList = [[] for i in range(n + 1)]
distList = [sys.maxsize] * (n + 1)
visit = [False] * (n + 1)

for i in range(m):
  start, end, cost = map(int, input().split())
  busList[start].append((end, cost))

depart, arrive = map(int, input().split())

def dijkstra(st, ed):
  queue = PriorityQueue()
  queue.put((0, st))
  distList[st] = 0
  while queue.qsize() > 0:
    now = queue.get()
    nowNode = now[1]
    if not visit[nowNode]:
      visit[nowNode] = True
      for i in busList[nowNode]:
        if not visit[i[0]] and distList[i[0]] > distList[nowNode] + i[1]:
          distList[i[0]] = distList[nowNode] + i[1]
          queue.put((distList[i[0]], i[0]))
  return distList[ed]

print(dijkstra(depart, arrive))