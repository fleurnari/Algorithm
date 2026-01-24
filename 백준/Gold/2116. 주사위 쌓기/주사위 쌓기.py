import sys
input = sys.stdin.readline
n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
opposite = [5, 3, 4, 1, 2, 0]
answer = 0

for bottomIdx in range(6):
  bottom = dice[0][bottomIdx]
  top = dice[0][opposite[bottomIdx]]
  total = max(dice[0][i] for i in range(6) if i != bottomIdx and i != opposite[bottomIdx])
  preTop = top
  for i in range(1, n):
    for j in range(6):
      if dice[i][j] == preTop:
        bottomIdx = j
        break
    top = dice[i][opposite[bottomIdx]]
    total += max(dice[i][k] for k in range(6) if k != bottomIdx and k != opposite[bottomIdx])
    preTop = top

  answer = max(answer, total)

print(answer)