import sys
input = sys.stdin.readline
mod = 1000000007
m = int(input())
cnt = 0

def cal(n, x):
  if x == 1:
    return n
  v = cal(n, x // 2)
  if x % 2 == 0:
    return v * v % mod
  else:
    return v * v * n % mod

for _ in range(m):
  n, s = map(int, input().split())
  rn = cal(n, mod - 2)
  cnt = (cnt + rn *s % mod) % mod

print(cnt)