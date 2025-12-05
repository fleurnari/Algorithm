import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
a = list(input())
a.pop()
b = list(input())
b.pop()
dpTable = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
result = []

for i in range(1, len(a) + 1):
  for j in range(1, len(b) + 1):
    if a[i - 1] == b[j - 1]:
      dpTable[i][j] = dpTable[i - 1][j - 1] + 1
    else:
      dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])

print(dpTable[-1][-1])

def getLCS(r, c):
  if r == 0 or c == 0:
    return
  if a[r - 1] == b[c - 1]:
    result.append(a[r - 1])
    getLCS(r - 1, c - 1)
  else:
    if dpTable[r - 1][c] > dpTable[r][c - 1]:
      getLCS(r - 1, c)
    else:
      getLCS(r, c - 1)

getLCS(len(a), len(b))

for i in range(len(result) - 1, -1, -1):
  print(result.pop(i), end = '')