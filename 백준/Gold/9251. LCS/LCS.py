import sys
input = sys.stdin.readline
a = list(input())
a.pop()
b = list(input())
b.pop()
dpTable = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]

for i in range(1, len(a) + 1):
  for j in range(1, len(b) + 1):
    if a[i - 1] == b[j - 1]:
      dpTable[i][j] = dpTable[i - 1][j - 1] + 1
    else:
      dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])

print(dpTable[len(a)][len(b)])