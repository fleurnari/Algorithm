import sys
input = sys.stdin.readline
a, b, n = map(int, input().split())
a = a % b

for _ in range(n):
  a *= 10
  digit = a // b
  a %= b

print(digit)