import sys
input = sys.stdin.readline
n, m = map(int, input().split())
treeHeight = 0
leafNodeCnt = n

while leafNodeCnt != 0:
  leafNodeCnt //= 2
  treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leafNodeStartIndex = treeSize // 2 - 1
treeList = [sys.maxsize] * (treeSize + 1)

for i in range(leafNodeStartIndex + 1, leafNodeStartIndex + n + 1):
  treeList[i] = int(input())

def setIdxTree(idx):
  while idx != 1:
    if treeList[idx // 2] > treeList[idx]:
      treeList[idx // 2] = treeList[idx]
    idx -= 1

setIdxTree(treeSize - 1)

def getMinValue(start, end):
  minValue = sys.maxsize
  while start <= end:
    if start % 2 == 1:
      minValue = min(minValue, treeList[start])
      start += 1
    if end % 2 == 0:
      minValue = min(minValue, treeList[end])
      end -= 1
    start = start // 2
    end = end // 2
  return minValue

for i in range(m):
  a, b = map(int, input().split())
  a = a + leafNodeStartIndex
  b = b + leafNodeStartIndex
  print(getMinValue(a, b))