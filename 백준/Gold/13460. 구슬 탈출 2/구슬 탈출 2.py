import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  graph.append(list(input()))
  for j in range(m):
    if graph[i][j] == 'R':
      rx, ry = i, j
    elif graph[i][j] == 'B':
      bx, by = i, j

def bfs(rx, ry, bx, by):
  queue = deque()
  queue.append((rx, ry, bx, by))
  visitList = []
  visitList.append((rx, ry, bx, by))
  cnt = 0
  while queue:
    for _ in range(len(queue)):
      rx, ry, bx, by = queue.popleft()
      if cnt > 10:
        print(-1)
        return
      if graph[rx][ry] == 'O':
        print(cnt)
        return
      for i in range(4):
        nrx, nry = rx, ry
        while True:
          nrx += dx[i]
          nry += dy[i]
          if graph[nrx][nry] == '#':
            nrx -= dx[i]
            nry -= dy[i]
            break
          if graph[nrx][nry] == 'O':
            break
        nbx, nby = bx, by
        while True:
          nbx += dx[i]
          nby += dy[i]
          if graph[nbx][nby] == '#':
            nbx -= dx[i]
            nby -= dy[i]
            break
          if graph[nbx][nby] == 'O':
            break
        if graph[nbx][nby] == 'O':
          continue
        if nrx == nbx and nry == nby:
          if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]
        if (nrx, nry, nbx, nby) not in visitList:
          queue.append((nrx, nry, nbx, nby))
          visitList.append((nrx, nry, nbx, nby))
    cnt += 1
  print(-1) 
    
bfs(rx, ry, bx, by)