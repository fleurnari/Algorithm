import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time = sys.maxsize
height = 0

for i in range(257):
  maxBlock, minBlock = 0, 0

  for j in range(n):
    for k in range(m):
      if arr[j][k] >= i:
        maxBlock += arr[j][k] - i
      else:
        minBlock += i - arr[j][k]

  if maxBlock + b >= minBlock:
    if maxBlock * 2 + minBlock <= time:
      time = maxBlock * 2 + minBlock
      height = i

print(time, height)