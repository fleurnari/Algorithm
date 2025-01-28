import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
treeList = [[0] for i in range(n + 1)]
depthList = [0] * (n + 1)
visitList = [False] * (n + 1)
tmp = 1
maxDepth = 0

for i in range(n - 1):
  start, end = map(int, input().split())
  treeList[start].append(end)
  treeList[end].append(start)

while tmp <= n:
  tmp <<= 1
  maxDepth += 1

parentList = [[0 for j in range(n + 1)] for i in range(maxDepth + 1)]

def bfs(node):
  queue = deque()
  queue.append(node)
  visitList[node] = True
  level = 1
  size = 1
  cnt = 0
  while queue:
    now = queue.popleft()
    for i in treeList[now]:
      if not visitList[i]:
        visitList[i] = True
        queue.append(i)
        parentList[0][i] = now
        depthList[i] = level
    cnt += 1
    if cnt == size:
      cnt = 0
      size = len(queue)
      level += 1
      
bfs(1)

for i in range(1, maxDepth + 1):
  for j in range(1, n + 1):
    parentList[i][j] = parentList[i - 1][parentList[i - 1][j]]

def lca(a, b):
  if depthList[a] > depthList[b]:
    tmp = a
    a = b
    b = tmp

  for i in range(maxDepth, -1, -1):
    if pow(2, i) <= depthList[b] - depthList[a]:
      if depthList[a] <= depthList[parentList[i][b]]:
        b = parentList[i][b]

  for i in range(maxDepth, -1, -1):
    if a == b:
      break
    if parentList[i][a] != parentList[i][b]:
      a = parentList[i][a]
      b = parentList[i][b]

  lcaNode = a
  if a != b:
    lcaNode = parentList[0][lcaNode]
    
  return lcaNode

m = int(input())
dicList = dict()

for i in range(m):
  a, b = map(int, input().split())
  if not dicList.get((a, b), 0):
    dicList[(a, b)] = dicList[(b, a)] = lca(a, b)
  print(str(dicList.get((a, b))))
  print("\n")