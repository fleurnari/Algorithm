import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
answer = [-1] * (n + 1)

for _ in range(m):
   u, v = map(int, input().split())
   graph[u].append(v)
   graph[v].append(u)

for i in range(n + 1):
   graph[i].sort(reverse = True)

def dfs(v, depth):
   visit[v] = True
   answer[v] = depth
   for i in graph[v]:
      if not visit[i]:
         dfs(i, depth + 1)

dfs(r, 0)

for i in range(1, n + 1):
   print(answer[i])