import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
tree = [[] for _ in range(n + 1)]
visitList = [-1] * (n + 1)
visitList[1] = 0

for _ in range(n - 1):
  a, b, c = map(int, input().split())
  tree[a].append((b, c))
  tree[b].append((a, c))

def dfs(start, dist):
  for next, nextDist in tree[start]:
    if visitList[next] == -1:
      visitList[next] = dist + nextDist
      dfs(next, dist + nextDist)

dfs(1, 0)

lastNode = visitList.index(max(visitList))
visitList = [-1] * (n + 1)
visitList[lastNode] = 0
dfs(lastNode, 0)

print(max(visitList))