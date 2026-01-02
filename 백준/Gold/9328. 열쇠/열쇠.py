import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(visitList):
  global answer
  queue = deque([[0, 0]])
  visitList[0][0] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= h + 2 or ny < 0 or ny >= w + 2 or building[nx][ny] == '*' or visitList[nx][ny]:
        continue

      if 'A' <= building[nx][ny] <= 'Z':
        if chr(ord(building[nx][ny]) + 32) not in keyList:
          continue
      elif 'a' <= building[nx][ny] <= 'z':
        if building[nx][ny] not in keyList:
          keyList[building[nx][ny]] = True
          visitList = [[False] * (w + 2) for _ in range(h + 2)]
      elif building[nx][ny] == "$" and (nx, ny) not in visitListIdx:
        answer += 1
        visitListIdx.append((nx, ny))

      visitList[nx][ny] = True
      queue.append([nx, ny])
        

for _ in range(1, t + 1):
  h, w = map(int, input().split())
  building = ['.' + input() + '.' for _ in range(h)]
  building = ['.' * (w + 2)] + building + ['.' * (w + 2)]
  visitList = [[False] * (w + 2) for _ in range(h + 2)]
  keyList = {}
  visitListIdx = []

  for i in input():
    if i.isalpha():
      keyList[i] = True

  answer = 0
  bfs(visitList)
  print(answer)