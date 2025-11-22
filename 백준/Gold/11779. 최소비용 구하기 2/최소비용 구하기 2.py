import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  s, e, w = map(int, input().split())
  graph[s].append((e, w))

start, end = map(int, input().split())
near = [start] * (n + 1)
dist = [sys.maxsize] * (n + 1)
queue = [(0, start)]

while queue:
  d, now = heapq.heappop(queue)
  if dist[now] < d:
    continue

  for next, nextDist in graph[now]:
    cost = nextDist + d
    if cost < dist[next]:
      dist[next], near[next] = cost, now
      heapq.heappush(queue, (cost, next))

answer = []
tmp = end
while tmp != start:
  answer.append(str(tmp))
  tmp = near[tmp]

answer.append(str(start))
answer.reverse()

print(dist[end])
print(len(answer))
print(" ".join(answer))