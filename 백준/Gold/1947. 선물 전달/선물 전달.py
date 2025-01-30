import sys
input = sys.stdin.readline
n = int(input())
mod = 1000000000
dpTable = [0] * 1000001
dpTable[1] = 0
dpTable[2] = 1

for i in range(3, n + 1):
  dpTable[i] = (i - 1) * (dpTable[i - 2] + dpTable[i - 1]) % mod

print(dpTable[n])