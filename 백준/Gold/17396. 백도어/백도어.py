import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(m):
   a, b, t = map(int, input().split())
   graph[a].append((b, t))
   graph[b].append((a, t))

dist = [sys.maxsize] * n
dist[0] = 0
queue = [(0, 0)]

while queue:
   cost, now = heapq.heappop(queue)
   if dist[now] < cost:
      continue
   for next, w in graph[now]:
      if arr[next] == 1 and next != n - 1:
         continue
      newCost = cost + w
      if newCost < dist[next]:
         dist[next] = newCost
         heapq.heappush(queue, (newCost, next))

print(dist[n - 1] if dist[n - 1] != sys.maxsize else -1)