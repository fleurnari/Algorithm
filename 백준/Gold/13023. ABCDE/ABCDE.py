import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for i in range(n + 1)]

visitList = [False] * (n + 1)

arrive = False


for i in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

def dfsDef(now, depth):
  global arrive
  if depth == 5:
    arrive = True
    return
  visitList[now] = True
  for i in arr[now]:
    if not visitList[i]:
      dfsDef(i, depth + 1)
  visitList[now] = False

for i in range(n):
  dfsDef(i, 1)
  if arrive:
    break

if arrive:
  print(1)
else:
  print(0)