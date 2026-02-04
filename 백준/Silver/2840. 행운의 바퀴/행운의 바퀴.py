import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [input().split() for _ in range(k)]
wheel = ['?'] * n
pos = 0
used = set()

for s, c in arr:
  s = int(s)
  pos = (pos + s) % n

  if wheel[pos] != '?' and wheel[pos] != c:
    print('!')
    sys.exit()

  if wheel[pos] == '?' and c in used:
    print('!')
    sys.exit()

  wheel[pos] = c
  used.add(c)

for i in range(n):
  print(wheel[(pos - i) % n], end = '')