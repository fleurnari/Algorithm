import tarfile
import sys
input = sys.stdin.readline
n = int(input())
dp = [False] * 1001
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5, n + 1):
    if not dp[i - 1]:
        dp[i] = True
    if not dp[i - 3]:
        dp[i] = True
    if not dp[i - 4]:
        dp[i] = True

print('SK' if dp[n] else 'CY')