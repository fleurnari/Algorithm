import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
visitList = [False] * (n + 1)

for _ in range(n - 1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

totalDepth = 0

def dfs(node, depth):
  global totalDepth
  visitList[node] = True
  isLeaf = True
  for i in tree[node]:
    if not visitList[i]:
      isLeaf = False
      dfs(i, depth + 1)
  if isLeaf:
    totalDepth += depth

dfs(1, 0)

if totalDepth % 2 == 1:
  print("Yes")
else:
  print("No")