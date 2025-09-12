import sys
input = sys.stdin.readline
k, n = map(int, input().split())
cmArr = []

for _ in range(k):
  cmArr.append(int(input()))

start = 1
end = max(cmArr)

while start <= end:
  mid = (start + end) // 2
  cnt = 0
  for i in cmArr:
    cnt += i // mid
  if cnt >= n:
    start = mid + 1
  else:
    end = mid - 1

print(end)