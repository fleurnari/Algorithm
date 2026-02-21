import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
order = [0] * (n + 1)

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(1, n + 1):
  graph[i].sort()

cnt = 1

def dfs(v):
  global cnt
  visited[v] = True
  order[v] = cnt
  cnt += 1
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

dfs(r)

for i in range(1, n + 1):
  print(order[i])