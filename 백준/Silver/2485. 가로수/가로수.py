import sys, math
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
g = 0

for i in range(1, n):
    g = math.gcd(g, abs(a[i] - a[i - 1]))

print((a[-1] - a[0]) // g + 1 - n)