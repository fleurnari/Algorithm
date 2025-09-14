import sys
input = sys.stdin.readline
n = int(input())
arr = []
result = []

for i in range(n):
  arr.append(list(map(int, input().split())))

def cutPaper(x, y, n):
  global result
  color = arr[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if color != arr[i][j]:
        cutPaper(x, y, n // 2)
        cutPaper(x, y + n // 2, n // 2)
        cutPaper(x + n // 2, y, n // 2)
        cutPaper(x + n // 2, y + n // 2, n // 2)
        return
  if color == 0:
    result.append(0)
  else:
    result.append(1)

cutPaper(0, 0, n)
print(result.count(0))
print(result.count(1))