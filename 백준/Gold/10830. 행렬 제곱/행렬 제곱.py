import sys
input = sys.stdin.readline
n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def mul(a, b):
  mulArr = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        mulArr[i][j] += a[i][k] * b[k][j] % 1000
  return mulArr

def square(mulArr, n):
  if n == 1:
    return mulArr
  tmp = square(mulArr, n // 2)
  if n % 2 == 0:
    return mul(tmp, tmp)
  else:
    return mul(mul(tmp, tmp), mulArr)

result = square(arr, b)
for i in range(n):
  for j in range(n):
    result[i][j] %= 1000

for i in result:
  print(*i)