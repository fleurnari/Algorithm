import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
treeHeight = 0
length = n
mod = 1000000007

while length != 0:
  length //= 2
  treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNode = treeSize // 2 - 1
seg = [1] * (treeSize + 1)

for i in range(leftNode + 1, leftNode + n + 1):
  seg[i] = int(input())

def setTree(i):
  while i != 1:
    seg[i // 2] = seg[i // 2] * seg[i] % mod
    i -= 1

setTree(treeSize - 1)

def changeValue(idx, value):
  seg[idx] = value
  while idx > 1:
    idx = idx // 2
    seg[idx] = seg[idx * 2] % mod * seg[idx * 2 + 1] % mod

def getMul(s, e):
  tmp = 1
  while s <= e:
    if s % 2 == 1:
      tmp = tmp * seg[s] % mod
      s += 1
    if e % 2 == 0:
      tmp = tmp * seg[e] % mod
      e -= 1
    s = s // 2
    e = e // 2
  return tmp

for _ in range(m + k):
  command, s, e = map(int, input().split())
  if command == 1:
    changeValue(leftNode + s, e)
  elif command == 2:
    s = leftNode + s
    e = leftNode + e
    print(getMul(s, e))