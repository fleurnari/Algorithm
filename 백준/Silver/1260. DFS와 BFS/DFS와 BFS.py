from collections import deque

n, m, v = map(int, input().split())

arr = [[] for i in range(n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

for i in range(n + 1):
  arr[i].sort()

def dfs(start):
  print(start, end = ' ')
  visitList[start] = True
  for i in arr[start]:
    if not visitList[i]:
      dfs(i)

visitList = [False] * (n + 1)
dfs(v)

def bfs(start):
  q = deque()
  q.append(start)
  visitList[start] = True

  while q:
    now = q.popleft()
    print(now, end = ' ')
    for i in arr[now]:
      if not visitList[i]:
        q.append(i)
        visitList[i] = True

print()
visitList = [False] * (n + 1)
bfs(v)