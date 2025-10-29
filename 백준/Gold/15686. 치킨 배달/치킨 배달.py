import sys
from itertools import combinations

n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
house = []
chicken = []

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      house.append((i, j))
    elif arr[i][j] == 2:
      chicken.append((i, j))

answer = sys.maxsize

for i in combinations(chicken, m):
  tmp = 0
  for j in house:
    eachTmp = sys.maxsize
    for k in range(m):
      eachTmp = min(eachTmp, abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]))
    tmp += eachTmp
  answer = min(answer, tmp)

print(answer)