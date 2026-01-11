import sys
input = sys.stdin.readline
n = int(input())
xList = []
yList = []
zList = []
edges = []
parentList = [i for i in range(n)]

for i in range(n):
  x, y, z = map(int, input().split())
  xList.append((x, i))
  yList.append((y, i))
  zList.append((z, i))

xList.sort()
yList.sort()
zList.sort()

for i in range(n - 1):
  edges.append((abs(xList[i][0] - xList[i + 1][0]), xList[i][1], xList[i + 1][1]))
  edges.append((abs(yList[i][0] - yList[i + 1][0]), yList[i][1], yList[i + 1][1]))
  edges.append((abs(zList[i][0] - zList[i + 1][0]), zList[i][1], zList[i + 1][1]))

edges.sort()

def find(x):
  if parentList[x] == x:
    return x
  parentList[x] = find(parentList[x])
  return parentList[x]

def union(a, b):
  a = find(a)
  b = find(b)
  if a < b:
    parentList[b] = a
  else:
    parentList[a] = b

def kruskal():
  idx = 0
  cnt = 0
  dist = 0
  while cnt < n - 1:
    w, a, b = edges[idx]
    idx += 1
    if find(a) == find(b):
      continue
    cnt += 1
    dist += w
    union(a, b)
  return dist

print(kruskal())