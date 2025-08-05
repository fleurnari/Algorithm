import sys
input = sys.stdin.readline
n = int(input())
level = 1
num = 1

while True:
  if n == 1:
    break
  level += 1
  if num >= n:
    break
  else:
    num += (level - 1) * 6

if n == 1:
  print(1)
else:
  print(level - 1)