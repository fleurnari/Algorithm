import sys
from queue import PriorityQueue

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
queue = PriorityQueue()
parentList = [0] * (n + 1)

for i in range(n + 1):
  parentList[i] = i

for i in range(m):
  a, b, c = map(int, input().split())
  queue.put((c, a, b))

def find(x):
  if x == parentList[x]:
    return x
  else:
    parentList[x] = find(parentList[x])
    return parentList[x]

def union(x1, x2):
  x1 = find(x1)
  x2 = find(x2)
  if x1 != x2:
    parentList[x2] = x1

edgeCnt = 0
result = 0

while edgeCnt < n - 1:
  c, a, b = queue.get()
  if find(a) != find(b):
    union(a, b)
    result += c
    edgeCnt += 1

print(result)