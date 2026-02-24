import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
prev = [-1] * n

for i in range(n):
  for j in range(i):
    if a[j] < a[i] and dp[j] + 1 > dp[i]:
      dp[i] = dp[j] + 1
      prev[i] = j

maxLen = max(dp)
idx = dp.index(maxLen)

result = []
while idx != -1:
  result.append(a[idx])
  idx = prev[idx]

result.reverse()

print(maxLen)
print(*result)