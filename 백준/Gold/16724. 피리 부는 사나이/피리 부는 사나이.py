import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
map = list(list(map(str, input().strip())) for _ in range(n))
visitList = [[-1 for _ in range(m)] for _ in range(n)]
safeZone = 0
direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
idx = 0

def move(x, y, idx):
  global safeZone
  if visitList[x][y] != -1:
    if visitList[x][y] == idx:
      safeZone += 1
    return

  visitList[x][y] = idx
  i = direction.index(map[x][y])
  move(x + dx[i], y + dy[i], idx)

for i in range(n):
  for j in range(m):
    move(i, j, idx)
    idx += 1

print(safeZone)