import math

a, b = map(int, input().split())

arr = [0] * (10000001)

count = 0

for i in range(2, len(arr)):
  arr[i] = i

for i in range(2, int(math.sqrt(len(arr)) + 1)):
  if arr[i] == 0:
    continue
  for j in range(i * i, len(arr), i):
    arr[j] = 0

for i in range(2, 10000001):
  if arr[i] != 0:
    n = arr[i]
    while arr[i] <= b / n:
      if arr[i] >= a / n:
        count += 1
      n = n * arr[i]

print(count)