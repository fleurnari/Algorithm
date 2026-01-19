import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
treeHeight = 0
length = n

while length != 0:
  length //= 2
  treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeIdx = treeSize // 2 - 1
tree = [0] * (treeSize + 1)

for i in range(leftNodeIdx + 1, leftNodeIdx + n + 1):
  tree[i] = int(input())

def setTree(i):
  while i != 1:
    tree[i // 2] += tree[i]
    i -= 1

setTree(treeSize - 1)

def changeValue(idx, value):
  diff = value - tree[idx]
  while idx > 0:
    tree[idx] = tree[idx] + diff
    idx = idx // 2

def getSum(s, e):
  tmp = 0
  while s <= e:
    if s % 2 == 1:
      tmp += tree[s]
      s += 1
    if e % 2 == 0:
      tmp += tree[e]
      e -= 1
    s = s // 2
    e = e // 2
  return tmp

for _ in range(m + k):
  command, s, e = map(int, input().split())
  if command == 1:
    changeValue(leftNodeIdx + s, e)
  elif command == 2:
    s = s + leftNodeIdx
    e = e + leftNodeIdx
    print(getSum(s, e))