import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
treeHeight = 0
leafNodeCnt = n

while leafNodeCnt != 0:
  leafNodeCnt //= 2
  treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leafNodeStartIdx = treeSize // 2 - 1
treeList = [0] * (treeSize + 1)

for i in range(leafNodeStartIdx + 1, leafNodeStartIdx + n + 1):
  treeList[i] = int(input())

def setIdxTree(idx):
  while idx != 1:
    treeList[idx // 2] += treeList[idx]
    idx -= 1

setIdxTree(treeSize - 1)

def changeValue(idx, val):
  diff = val - treeList[idx]
  while idx > 0:
    treeList[idx] = treeList[idx] + diff
    idx = idx // 2

def getPartSum(start, end):
  partSum = 0
  while start <= end:
    if start % 2 == 1:
      partSum += treeList[start]
      start += 1
    if end % 2 == 0:
      partSum += treeList[end]
      end -= 1
    start = start // 2
    end = end // 2
  return partSum

for i in range(m + k):
  a, b, c = map(int, input().split())
  if a == 1:
    changeValue(leafNodeStartIdx + b, c)
  elif a == 2:
    b = b + leafNodeStartIdx
    c = c + leafNodeStartIdx
    print(getPartSum(b, c))