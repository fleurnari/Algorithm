import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dpTable = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dpTable[0][1][0] = 1

for i in range(n):
  for j in range(n):
    type1, type2, type3 = 0, 0, 0
    if arr[i][j] == 0 and (i, j) != (0, 1):
      if j >= 1:
        type1 += (dpTable[i][j - 1][0] + dpTable[i][j - 1][2])
      if i >= 1:
        type2 += (dpTable[i - 1][j][1] + dpTable[i - 1][j][2])
      if i >= 1 and j >= 1:
        if arr[i - 1][j] != 1 and arr[i][j - 1] != 1:
          type3 += sum(dpTable[i - 1][j - 1])
      dpTable[i][j] = [type1, type2, type3]

print(sum(dpTable[-1][-1]))