import sys
import heapq
inf = sys.maxsize
input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start))
  dist = [inf] * (n + 1)
  dist[start] = 0
  while queue:
    d, now = heapq.heappop(queue)
    if dist[now] < d:
      continue
    for v, w in graph[now]:
        cost = d + w
        if cost < dist[v]:
          dist[v] = cost
          heapq.heappush(queue, (cost, v))
  return dist

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())
d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)
result = min(d1[v1] + d2[v2] + d3[n], d1[v2] + d3[v1] + d2[n])
print(result if result < inf else -1)