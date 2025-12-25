import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
arr = [0]

def binarySearch(x):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] < x:
      start = mid + 1
    else:
      end = mid - 1
  return start

for i in range(n):
  if arr[-1] < a[i]:
    arr.append(a[i])
  elif arr[-1] > a[i]:
    idx = binarySearch(a[i])
    arr[idx] = a[i]

print(len(arr) - 1)