import sys
input = sys.stdin.readline
n = int(input())
x = []
y = []
result = 0

for i in range(n):
  tmpX, tmpY = map(int, input().split())
  x.append(tmpX)
  y.append(tmpY)

x.append(x[0])
y.append(y[0])

for i in range(n):
  result += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

print(round(abs(result / 2), 1))