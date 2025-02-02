import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
seq = [0] * 1000001
dpTable = [0] * 1000001
result = [0] * 1000001
idx = 0
maxLength = 1
seq[maxLength] = a[1]
dpTable[1] = 1

def bs(left, right, now):
  while left < right:
    mid = (left + right) // 2
    if seq[mid] < now:
      left = mid + 1
    else:
      right = mid
  return left

for i in range(2, n + 1):
  if seq[maxLength] < a[i]:
    maxLength += 1
    seq[maxLength] = a[i]
    dpTable[i] = maxLength
  else:
    idx = bs(1, maxLength, a[i])
    seq[idx] = a[i]
    dpTable[i] = idx

print(maxLength)
idx = maxLength

for i in range(n, 0, -1):
  if dpTable[i] == idx:
    result[idx] = a[i]
    idx -= 1

for i in range(1, maxLength + 1):
  print(result[i], end = ' ')