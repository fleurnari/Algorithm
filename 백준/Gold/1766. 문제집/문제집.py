import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
problem = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
queue =  []
result = []

for _ in range(m):
  a, b = map(int, input().split())
  problem[a].append(b)
  indegree[b] += 1

for i in range(1, n + 1):
  if indegree[i] == 0:
    heapq.heappush(queue, i)

while queue:
  now = heapq.heappop(queue)
  result.append(now)
  for i in problem[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      heapq.heappush(queue, i)

print(" ".join(map(str, result)))