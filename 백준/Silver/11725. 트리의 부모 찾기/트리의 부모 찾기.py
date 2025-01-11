import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
visitList = [False] * (n + 1)
treeList = [[] for i in range(n + 1)]
answerList = [0] * (n + 1)

for i in range(1, n):
  node1, node2 = map(int, input().split())
  treeList[node1].append(node2)
  treeList[node2].append(node1)

def dfs(num):
  visitList[num] = True
  for i in treeList[num]:
    if not visitList[i]:
      answerList[i] = num
      dfs(i)

dfs(1)

for i in range(2, n + 1):
  print(answerList[i])