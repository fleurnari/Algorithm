import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for i in range(n + 1)]

answer = [0] * (n + 1)

for i in range(m):
  start, end = map(int, input().split())
  arr[start].append(end)

def bfs(v):
  visit = [False] * (n + 1)
  q = deque()
  q.append(v)
  visit[v] = True
  while q:
    now = q.popleft()
    for i in arr[now]:
      if not visit[i]:
        visit[i] = True
        answer[i] += 1
        q.append(i)

for i in range(1, n + 1):
  bfs(i)

maxC = max(answer)

for i in range(1, n + 1):
  if answer[i] == maxC:
    print(i, end = ' ')