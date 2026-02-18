import sys
input = sys.stdin.readline
n, t = map(int, input().split())
unit = {}
dp = [0] * (t + 1)

for i in range(1, n + 1):
  k, s = map(int, input().split())
  unit[i] = (k, s)

for i in range(1, n + 1):
  k, s = unit[i]
  for j in range(t, k - 1, -1):
    dp[j] = max(dp[j], dp[j - k] + s)

print(dp[t])