import sys
input = sys.stdin.readline
n = int(input())
arr = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
  arr[i] = list(map(int, input().split()))

for k in range(n):
  for i in range(n):
    for j in range(n):
      if arr[i][k] == 1 and arr[k][j] == 1:
        arr[i][j] = 1

for i in range(n):
  for j in range(n):
    print(arr[i][j], end= ' ')
  print()