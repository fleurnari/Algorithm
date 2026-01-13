import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
idx = 0
maxLength = 1
best = [0] * 1000001
dpTable = [0] * 1000001
answer = [0] * 1000001
best[maxLength] = a[1]
dpTable[1] = 1

def binarySearch(l, r, now):
  while l < r:
    mid = (l + r) // 2
    if best[mid] < now:
      l = mid + 1
    else:
      r = mid
  return l

for i in range(2, n + 1):
  if best[maxLength] < a[i]:
    maxLength += 1
    best[maxLength] = a[i]
    dpTable[i] = maxLength
  else:
    idx = binarySearch(1, maxLength, a[i])
    best[idx] = a[i]
    dpTable[i] = idx

print(maxLength)
idx = maxLength

for i in range(n, 0, -1):
  if dpTable[i] == idx:
    answer[idx] = a[i]
    idx -= 1

for i in range(1, maxLength + 1):
  print(answer[i], end = ' ')