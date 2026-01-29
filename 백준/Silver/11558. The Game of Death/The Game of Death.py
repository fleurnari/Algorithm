import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  a = [int(input()) for _ in range(n)]
  visitList = [False] * (n + 1)
  current = 1
  cnt = 0
  while True:
    if current == n:
      print(cnt)
      break
    if visitList[current]:
      print(0)
      break
    visitList[current] = True
    current = a[current - 1]
    cnt += 1