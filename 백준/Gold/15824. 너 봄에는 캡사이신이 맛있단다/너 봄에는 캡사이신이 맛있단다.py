import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0
mod = 1000000007

def pow(a, b):
  if b == 0:
    return 1
  if b == 1:
    return a
  half = pow(a, b // 2)
  if b % 2 == 0:
    return half * half % mod
  else:
    return half * half * a % mod

for i in range(n):
  answer += arr[i] * (pow(2, i) - pow(2, n - i - 1))

print(answer % mod)