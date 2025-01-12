import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
parentList = list(map(int, input().split()))
deleteNode = int(input())
treeList = [[] for i in range(n)]
visitList = [False] * n
rootNode = 0
result = 0

for i in range(n):
  if parentList[i] != -1:
    treeList[i].append(parentList[i])
    treeList[parentList[i]].append(i)
  else:
    rootNode = i

def dfs(num):
  global result
  visitList[num] = True
  childNode = 0
  for i in treeList[num]:
    if not visitList[i] and i != deleteNode:
      childNode += 1
      dfs(i)
  if childNode == 0:
    result += 1

if deleteNode == rootNode:
  print(0)
else:
  dfs(rootNode)
  print(result)