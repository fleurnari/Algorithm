import math

n = int(input())

arr = [0] * (10000001)

for i in range(2, len(arr)):
  arr[i] = i

for i in range(2, int(math.sqrt(len(arr)) + 1)):
  if arr[i] == 0:
    continue
  for j in range(i * i, len(arr), i):
    arr[j] = 0

def pldr(num):
  tmp = list(str(num))
  start = 0
  end = len(tmp) - 1

  while start < end:
    if tmp[start] != tmp[end]:
      return False
    start += 1
    end -= 1

  return True

i = n

while True:
  if arr[i] != 0:
    num = arr[i]
    if pldr(num):
      print(num)
      break
      
  i += 1