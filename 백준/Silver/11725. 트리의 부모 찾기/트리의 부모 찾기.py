import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
visitList = [False] * (n + 1)
arr = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for _ in range(1, n):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

def dfs(v):
  visitList[v] = True
  for i in arr[v]:
    if not visitList[i]:
      answer[i] = v
      dfs(i)

dfs(1)

for i in range(2, n + 1):
  print(answer[i])