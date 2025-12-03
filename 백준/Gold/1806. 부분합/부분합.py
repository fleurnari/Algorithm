import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
sum = 0
minLength = sys.maxsize

while True:
  if sum >= s:
    minLength = min(minLength, right - left)
    sum -= arr[left]
    left += 1
  elif right == n:
    break
  else:
    sum += arr[right]
    right += 1

if minLength == sys.maxsize:
  print(0)
else:
  print(minLength)