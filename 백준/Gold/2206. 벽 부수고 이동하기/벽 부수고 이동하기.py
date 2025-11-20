import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(n)]
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visitList = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
  queue = deque()
  queue.append([0, 0, 0])
  visitList[0][0][0] = 1
  while queue:
    x, y, z = queue.popleft()
    if x == n - 1 and y == m - 1:
      return visitList[x][y][z] 
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if 0 <= nx < n and 0 <= ny < m:
        if map[nx][ny] == 0 and visitList[nx][ny][z] == 0:
          visitList[nx][ny][z] = visitList[x][y][z] + 1
          queue.append((nx, ny, z))
        elif map[nx][ny] == 1 and z == 0:
          visitList[nx][ny][z + 1] = visitList[x][y][z] + 1
          queue.append((nx, ny, z + 1))
  return -1

print(bfs())