import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
treeList = [[] for i in range(n + 1)]
depthList = [0] * (n + 1)
parentList = [0] * (n + 1)
visitList = [False] * (n + 1)

for i in range(n - 1):
  start, end = map(int, input().split())
  treeList[start].append(end)
  treeList[end].append(start)

def bfs(node):
  queue = [node]
  visitList[node] = True
  while queue:
    now = queue.pop(0)
    for i in treeList[now]:
      if not visitList[i]:
        visitList[i] = True
        queue.append(i)
        parentList[i] = now
        depthList[i] = depthList[now] + 1

bfs(1)


def lca(a, b):
  if depthList[a] < depthList[b]:
    tmp = a
    a = b
    b = tmp

  while depthList[a] != depthList[b]:
    a = parentList[a]

  while a != b:
    a = parentList[a]
    b = parentList[b]

  return a

m = int(input())
dicList = dict()

for i in range(m):
  a, b = map(int, input().split())
  if not dicList.get((a, b), 0):
    dicList[(a, b)] = dicList[(b, a)] = lca(a, b)
  print(str(dicList.get((a, b))))
  print("\n")