n = int(input())
dpTable = [0] * 1001
dpTable[1] = 1
dpTable[2] = 2
mod = 10007

for i in range(3, n + 1):
  dpTable[i] = (dpTable[i - 1] + dpTable[i - 2]) % mod

print(dpTable[n])