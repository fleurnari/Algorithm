import sys
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
board = []
answer = 0

for _ in range(n):
  board.append(list(map(int, input().split())))

def left(board):
  for i in range(n):
    cursor = 0
    for j in range(n):
      if board[i][j] != 0:
        tmp = board[i][j]
        board[i][j] = 0
        if not board[i][cursor]:
          board[i][cursor] = tmp
        elif board[i][cursor] == tmp:
          board[i][cursor] *= 2
          cursor += 1
        else:
          cursor += 1
          board[i][cursor] = tmp
  return board

def right(board):
  for i in range(n):
    cursor = n - 1
    for j in range(n - 1, -1, -1):
      if board[i][j] != 0:
        tmp = board[i][j]
        board[i][j] = 0
        if board[i][cursor] == 0:
          board[i][cursor] = tmp
        elif board[i][cursor] == tmp:
          board[i][cursor] *= 2
          cursor -= 1
        else:
          cursor -= 1
          board[i][cursor] = tmp
  return board

def up(board):
  for j in range(n):
    cursor = 0
    for i in range(n):
      if board[i][j] != 0:
        tmp = board[i][j]
        board[i][j] = 0
        if board[cursor][j] == 0:
          board[cursor][j] = tmp
        elif board[cursor][j] == tmp:
          board[cursor][j] *= 2
          cursor += 1
        else:
          cursor += 1
          board[cursor][j] = tmp
  return board

def down(board):
  for j in range(n):
    cursor = n - 1
    for i in range(n - 1, -1, -1):
      if board[i][j] != 0:
        tmp = board[i][j]
        board[i][j] = 0
        if board[cursor][j] == 0:
          board[cursor][j] = tmp
        elif board[cursor][j] == tmp:
          board[cursor][j] *= 2
          cursor -= 1
        else:
          cursor -= 1
          board[cursor][j] = tmp
  return board

def dfs(x, board):
  global answer
  if x == 5:
    for i in range(n):
      for j in range(n):
        if board[i][j] > answer:
          answer = board[i][j]
    return

  for i in range(4):
    copyBoard = deepcopy(board)
    if i == 0:
      dfs(x + 1, left(copyBoard))
    elif i == 1:
      dfs(x + 1, right(copyBoard))
    elif i == 2:
      dfs(x + 1, up(copyBoard))
    else:
      dfs(x + 1, down(copyBoard))

dfs(0, board)
print(answer)