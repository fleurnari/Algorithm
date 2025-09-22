import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[sys.maxsize for j in range(n + 1)] for i in range(n + 1)]
min = sys.maxsize
result = 0

for i in range(1, n + 1):
  arr[i][i] = 0

for i in range(m):
  a, b = map(int, input().split())
  arr[a][b] = 1
  arr[b][a] = 1

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if arr[i][j] > arr[i][k] + arr[k][j]:
        arr[i][j] = arr[i][k] + arr[k][j]

for i in range(1, n + 1):
  tmp = 0
  for j in range(1, n + 1):
    tmp += arr[i][j]
  if min > tmp:
    min = tmp
    result = i

print(result)