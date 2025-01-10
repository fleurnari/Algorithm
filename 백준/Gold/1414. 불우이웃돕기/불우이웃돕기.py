import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())
queue = PriorityQueue()
sum = 0
edgeCnt = 0
result = 0

parentList = [0] * n

for i in range(n):
  parentList[i] = i

for i in range(n):
  tmpList = list(input())
  for j in range(n):
    tmp = 0
    if 'a' <= tmpList[j] <= 'z':
      tmp = ord(tmpList[j]) - ord('a') + 1
    elif 'A' <= tmpList[j] <= 'Z':
      tmp = ord(tmpList[j]) - ord('A') + 27
    sum += tmp
    if i != j and tmp != 0:
      queue.put((tmp, i, j))

def find(a):
  if a == parentList[a]:
    return a
  else:
    parentList[a] = find(parentList[a])
    return parentList[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parentList[b] = a

while queue.qsize() > 0:
  llLength, start, end = queue.get()
  if find(start) != find(end):
    union(start, end)
    result += llLength
    edgeCnt += 1
    
if edgeCnt == n - 1:
  print(sum - result)
else:
  print(-1)