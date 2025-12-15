import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
tmpValue = sys.maxsize

for i in range(n - 2):
  start = i + 1
  end = n - 1
  while start < end:
    tmp = arr[i] + arr[start] + arr[end]
    if abs(tmp) < tmpValue:
      tmpValue = abs(tmp)
      result = [arr[i], arr[start], arr[end]]
    if tmp < 0:
      start += 1
    elif tmp > 0:
      end -= 1
    else:
      break

print(result[0], result[1], result[2])