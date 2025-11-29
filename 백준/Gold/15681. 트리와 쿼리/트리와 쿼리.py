import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visitList = [-1 for _ in range(n + 1)]

for _ in range(n - 1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(current):
  global visitList
  visitList[current] = 1
  for i in graph[current]:
    if visitList[i] == -1:
      visitList[current] += dfs(i)
  return visitList[current]

dfs(r)

for _ in range(q):
  node = int(input())
  print(visitList[node])