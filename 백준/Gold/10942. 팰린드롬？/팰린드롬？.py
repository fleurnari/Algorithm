import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dpTable = [[0] * n for _ in range(n)]

for i in range(n):
  dpTable[i][i] = 1
for i in range(n - 1):
  if arr[i] == arr[i + 1]:
    dpTable[i][i + 1] = 1
  else:
    dpTable[i][i + 1] = 0
for k in range(n - 2):
  for i in range(n - 2 - k):
    j = i + 2 + k
    if arr[i] == arr[j] and dpTable[i + 1][j - 1] == 1:
      dpTable[i][j] = 1
      
m = int(input())
for _ in range(m):
  s, e = map(int, input().split())
  print(dpTable[s - 1][e - 1])