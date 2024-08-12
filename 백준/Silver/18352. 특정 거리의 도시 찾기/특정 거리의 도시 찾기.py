import sys

from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

arr = [[] for i in range(n + 1)]

visit = [-1] * (n + 1)

result = []


for i in range(m):
  start, end = map(int, input().split())
  arr[start].append(end)

def bfs(v):
  q = deque()
  q.append(v)
  visit[v] += 1
  while q:
    now = q.popleft()
    for i in arr[now]:
      if visit[i] == -1:
        visit[i] = visit[now] + 1
        q.append(i)

bfs(x)

for i in range(n + 1):
  if visit[i] == k:
    result.append(i)

if not result:
  print(-1)
else:
  result.sort()
  for i in result:
    print(i)