import sys
from copy import deepcopy
input = sys.stdin.readline
R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
answer = 0

for _ in range(M):
  r, c, s, d, z = map(int, input().split())
  board[r - 1][c - 1] = [s, d, z]

def move(i, j, speed, direct):
  dx, dy = dir[direct - 1]
  if direct == 1 or direct == 2:
    speed = speed % ((R - 1) * 2)
  elif direct == 3 or direct == 4:
    speed = speed % ((C - 1) * 2)
  while True:
    if -1 < i + dx * speed < R and -1 < j + dy * speed < C:
      return i + dx * speed, j + dy * speed, direct
    if direct == 1:
      speed -= i
      dx, dy = 1, 0
      i = 0
      direct = 2
    elif direct == 2:
      speed -= R - 1 - i
      dx, dy = -1, 0
      i = R - 1
      direct = 1
    elif direct == 3:
      speed -= C - 1 - j
      dx, dy = 0, -1
      j = C - 1
      direct = 4
    elif direct == 4:
      speed -= j
      dx, dy = 0, 1
      j = 0
      direct = 3

for j in range(C):
  for i in range(R):
    if board[i][j] != 0:
      answer += board[i][j][2]
      board[i][j] = 0
      break

  newBoard = [[0] * C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if board[i][j] != 0:
        speed = board[i][j][0]
        nx, ny, direct = move(i, j, speed, board[i][j][1])
        if newBoard[nx][ny] == 0:
          newBoard[nx][ny] = [board[i][j][0], direct, board[i][j][2]]
        else:
          if newBoard[nx][ny][2] < board[i][j][2]:
            newBoard[nx][ny] = [board[i][j][0], direct, board[i][j][2]]
  board = deepcopy(newBoard)

print(answer)
