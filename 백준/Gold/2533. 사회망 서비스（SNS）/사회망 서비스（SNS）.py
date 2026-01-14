import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
dpTable = [[0, 0] for _ in range(n + 1)]
visitList = [False for _ in range(n + 1)]

for _ in range(n - 1):
  u, v = map(int, input().split())
  tree[u].append(v)
  tree[v].append(u)

def dfs(start):
  global tree
  global visitList
  visitList[start] = True
  if len(tree[start]) == 0:
    dpTable[start][1] = 1
    dpTable[start][0] = 0
  else:
    for i in tree[start]:
      if not visitList[i]:
        dfs(i)
        dpTable[start][1] += min(dpTable[i][0], dpTable[i][1])
        dpTable[start][0] += dpTable[i][1]
    dpTable[start][1] += 1

dfs(1)
print(min(dpTable[1][0], dpTable[1][1]))