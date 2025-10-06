import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [0] * 101
visitList = [False] * 101

ladder = dict()
snake = dict()

for i in range(n):
  x, y = map(int, input().split())
  ladder[x] = y 

for i in range(m):
  u, v = map(int, input().split())
  snake[u] = v

queue = deque([1])

while queue:
  x = queue.popleft()
  if x == 100:
    print(board[x])
    break
  for i in range(1, 7):
    nx = x + i
    if nx <= 100 and not visitList[nx]:
      if nx in ladder.keys():
        nx = ladder[nx]
      if nx in snake.keys():
        nx = snake[nx]
      if not visitList[nx]:
        visitList[nx] = True
        board[nx] = board[x] + 1
        queue.append(nx)