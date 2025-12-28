import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
c = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]
friend = [1 for _ in range(n + 1)]

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b):
  a = find(a)
  b = find(b)
  if a < b:
    a, b = b, a
  parent[a] = b

for _ in range(m):
  a, b = map(int, input().split())
  union(a, b)

for i in range(1, n + 1):
  if i != parent[i]:
    friend[find(i)] += 1
    c[find(i)] += c[i]

parents = [i for i in set(parent)]
parentNum = len(parents)
dpTable = [[0 for _ in range(k)] for _ in range(parentNum)]

for i in range(1, parentNum):
  for j in range(k):
    x = parents[i]
    if j < friend[x]:
      dpTable[i][j] = dpTable[i - 1][j]
    else:
      dpTable[i][j] = max(dpTable[i - 1][j - friend[x]] + c[x], dpTable[i - 1][j])

print(dpTable[-1][-1])