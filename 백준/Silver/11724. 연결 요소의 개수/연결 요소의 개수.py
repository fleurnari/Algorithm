import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visitList = [False] * (n + 1)
result = 0

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(v):
  visitList[v] = True
  for i in graph[v]:
    if not visitList[i]:
      dfs(i)

for i in range(1, n + 1):
  if  not visitList[i]:
    result += 1
    dfs(i)

print(result)