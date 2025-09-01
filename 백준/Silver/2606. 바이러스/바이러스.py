import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
computerList = [[] for i in range(n + 1)]
visitList = [False] * (n + 1)

for i in range(1, m + 1):
  a, b = map(int, input().split())
  computerList[a].append(b)
  computerList[b].append(a)

def dfs(v):
  visitList[v] = True
  for i in computerList[v]:
    if not visitList[i]:
      visitList[i] = True
      dfs(i)


dfs(1)

print(visitList.count(True) - 1)