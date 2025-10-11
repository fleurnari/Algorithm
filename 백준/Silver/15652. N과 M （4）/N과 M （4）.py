import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = []

def dfs(x):
  if len(s) == m:
    print(*s)
    return

  for i in range(x, n + 1):
      s.append(i)
      dfs(i)
      s.pop()

dfs(1)