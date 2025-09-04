import sys
input = sys.stdin.readline
t = int(input())
p = [0] * (101)
p[1:5] = [1, 1, 1, 2, 2]

for i in range(6, 101):
  p[i] = p[i - 1] + p[i - 5]

for i in range(t):
  n = int(input())
  print(p[n])