import sys

input = sys.stdin.readline
a, b = map(int, input().split())
answer = 1

while a != b:
  answer += 1
  tmp = b

  if b % 10 == 1:
    b //= 10
  elif b % 2 == 0:
    b //= 2

  if tmp == b:
    answer = -1
    break

print(answer)