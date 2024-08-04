import math

min, max = map(int, input().split())

arr = [False] * (max - min + 1)

count = 0

for i in range(2, int(math.sqrt(max) + 1)):
  pow = i * i
  start = int(min / pow)
  if min % pow != 0:
    start += 1

  for j in range(start, int(max / pow) + 1):
    arr[int((j * pow) - min)] = True

for i in range(0, max - min + 1):
  if not arr[i]:
    count += 1

print(count)