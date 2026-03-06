import sys
input = sys.stdin.readline
t = int(input())
mod = 1000000007
max = 2500
dp = [0] * (max + 1)
dp[0] = 1

for i in range(1, max + 1):
   for j in range(i):
      dp[i] = (dp[i] + dp[j] * dp[i - j - 1]) % mod

for _ in range(t):
   l = int(input())
   if l % 2 == 1:
      print(0)
   else:
      print(dp[l // 2])