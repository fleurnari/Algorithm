import sys
input = sys.stdin.readline
n = int(input())
visited = [False] * (n + 1)
path = []

def dfs():
  if len(path) == n:
    print(*path)
    return

  for i in range(1, n + 1):
    if not visited[i]:
      visited[i] = True
      path.append(i)
      dfs()
      path.pop()
      visited[i] = False

dfs()