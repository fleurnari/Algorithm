import sys
import heapq
input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = 0

for _ in range(m):
  s, e, t = map(int, input().split())
  graph[s].append((e, t))

def dijkstra(start):
  queue = []
  dist = [sys.maxsize] * (n + 1)
  heapq.heappush(queue, (0, start))
  dist[start] = 0

  while queue:
    d, now = heapq.heappop(queue)
    if dist[now] < d:
      continue

    for idx, time in graph[now]:
      cost = d + time
      if cost < dist[idx]:
        dist[idx] = cost
        heapq.heappush(queue, (cost, idx))

  return dist

back = dijkstra(x)

for i in range(1, n + 1):
  go = dijkstra(i)
  result = max(result, go[x] + back[i])

print(result)