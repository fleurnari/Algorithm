import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  a, b = arr[i]
  arr[i] = [min(a, b), max(a, b)]

arr.sort(key=lambda x: (x[0], x[1]))
dp = [1] * n

for i in range(n):
  for j in range(i):
    if arr[i][1] >= arr[j][1]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))