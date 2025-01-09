import sys
import copy
from collections import deque
from queue import PriorityQueue
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
mapList = [[0 for j in range(m)] for i in range(n)]
visitList = [[False for j in range(m)] for i in range(n)]

for i in range(n):
  mapList[i] = list(map(int, input().split()))

ilNum = 1
ilList = list([])
island = []

def addNode(i, j, q):
  mapList[i][j] = ilNum
  visitList[i][j] = True
  tmp = [i, j]
  island.append(tmp)
  q.append(tmp)

def bfs(i, j):
  q = deque()
  island.clear()
  start = [i, j]
  q.append(start)
  island.append(start)
  visitList[i][j] = True
  mapList[i][j] = ilNum
  while q:
    r, c = q.popleft()
    for i in range(4):
      tmpR = dr[i]
      tmpC = dc[i]
      while r + tmpR >= 0 and r + tmpR < n and c + tmpC >= 0 and c + tmpC < m:
        if not visitList[r + tmpR][c + tmpC] and mapList[r + tmpR][c + tmpC] != 0:
          addNode(r + tmpR, c + tmpC, q)
        else:
          break
        if tmpR < 0:
          tmpR -= 1
        elif tmpR > 0:
          tmpR += 1
        elif tmpC < 0:
          tmpC -= 1
        elif tmpC > 0:
          tmpC += 1
  return island

for i in range(n):
  for j in range(m):
    if mapList[i][j] != 0 and not visitList[i][j]:
      tmpList = copy.deepcopy(bfs(i, j))
      ilNum += 1
      ilList.append(tmpList)

queue = PriorityQueue()

for now in ilList:
  for tmp in now:
    r = tmp[0]
    c = tmp[1]
    nowIsland = mapList[r][c]
    for i in range(4):
      tmpR = dr[i]
      tmpC = dc[i]
      seaLength = 0
      while r + tmpR >= 0 and r + tmpR < n and c + tmpC >= 0 and c + tmpC < m:
        if mapList[r + tmpR][c + tmpC] == nowIsland:
          break
        elif mapList[r + tmpR][c + tmpC] != 0:
          if seaLength > 1:
            queue.put((seaLength, nowIsland, mapList[r + tmpR][c + tmpC]))
          break
        else:
          seaLength += 1
        if tmpR < 0:
          tmpR -= 1
        elif tmpR > 0:
          tmpR += 1
        elif tmpC < 0:
          tmpC -= 1
        elif tmpC > 0:
          tmpC += 1

parentList = [0] * ilNum

for i in range(len(parentList)):
  parentList[i] = i

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

edgeCnt = 0
result = 0

while queue.qsize() > 0:
  v, s, e = queue.get()
  if find(s) != find(e):
    union(s, e)
    result += v
    edgeCnt += 1

if edgeCnt == ilNum - 2:
  print(result)
else:
  print(-1)