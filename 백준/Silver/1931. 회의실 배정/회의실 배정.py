n = int(input())

arr = [[0] * 2 for i in range(n)]

answer = 0

for i in range(n):
  start, end = map(int, input().split())
  arr[i][0] = end
  arr[i][1] = start

arr.sort()

endTime = -1

for i in range(n):
  if arr[i][1] >= endTime:
    endTime = arr[i][0]
    answer += 1

print(answer)