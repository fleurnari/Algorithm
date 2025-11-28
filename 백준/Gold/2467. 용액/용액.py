import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
start = 0
end = n - 1
answer = abs(arr[start] + arr[end])
anStart = start
anEnd = end

while start < end:
  tmp = arr[start] + arr[end]
  
  if abs(tmp) <= answer:
    answer = abs(tmp)
    anStart = start
    anEnd = end

    if answer == 0:
      break

  if tmp < 0:
    start += 1
  else:
    end -= 1

print(arr[anStart], arr[anEnd])