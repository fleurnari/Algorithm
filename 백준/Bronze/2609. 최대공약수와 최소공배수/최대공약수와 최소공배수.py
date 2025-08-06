import sys
input = sys.stdin.readline
n, m = map(int, input().split())

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

print(int(gcd(n, m)))
print(int(n * m / gcd(n, m)))