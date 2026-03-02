import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 1000001
dp[1] = 1
mod = 1000000007

for i in range(2, n + 1):
   dp[i] = (dp[i - 1] + dp[i - 2]) % mod

print(dp[n])