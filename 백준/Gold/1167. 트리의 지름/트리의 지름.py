import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v = int(input())
tree = [[] for _ in range(v + 1)]
visitList = [-1] * (v + 1)
visitList[1] = 0

for _ in range(v):
  command = list(map(int, input().split()))
  node = command[0]
  idx = 1
  while command[idx] != -1:
    tree[node].append((command[idx], command[idx + 1]))
    idx += 2


def dfs(node, dist):
  for n, d in tree[node]:
    newDist = dist + d
    if visitList[n] == -1:
      visitList[n] = newDist
      dfs(n, newDist)
  return

dfs(1, 0)
tmp = [0, 0]
for i in range(1, len(visitList)):
  if visitList[i] > tmp[1]:
    tmp[1] = visitList[i]
    tmp[0] = i

visitList = [-1] * (v + 1)
visitList[tmp[0]] = 0
dfs(tmp[0], 0)

print(max(visitList))