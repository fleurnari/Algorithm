import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
treeHeight = 0
leafNodeCnt = n
mod = 1000000007

while leafNodeCnt != 0:
  leafNodeCnt //= 2
  treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leafNodeStartIdx = treeSize // 2 - 1
treeList = [1] * (treeSize + 1)

for i in range(leafNodeStartIdx + 1, leafNodeStartIdx + n + 1):
  treeList[i] = int(input())

def setIdxTree(idx):
  while idx != 1:
    treeList[idx // 2] = treeList[idx // 2] * treeList[idx] % mod
    idx -= 1

setIdxTree(treeSize - 1)

def changeValue(idx, val):
  treeList[idx] = val
  while idx > 1:
    idx = idx // 2
    treeList[idx] = treeList[idx * 2] % mod * treeList[idx * 2 + 1] % mod

def getPartMul(start, end):
  partMul = 1
  while start <= end:
    if start % 2 == 1:
      partMul = partMul * treeList[start] % mod
      start += 1
    if end % 2 == 0:
      partMul = partMul * treeList[end] % mod
      end -= 1
    start = start // 2
    end = end // 2
  return partMul

for i in range(m + k):
  a, b, c = map(int, input().split())
  if a == 1:
    changeValue(leafNodeStartIdx + b, c)
  if a == 2:
    b = b + leafNodeStartIdx
    c = c + leafNodeStartIdx
    print(getPartMul(b, c))