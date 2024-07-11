import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, m = map(int, input().split())

a = [[] for i in range(n + 1)]

visitList = [False] * (n + 1)

answer = 0

for i in range(m):
  u, v = map(int, input().split())
  a[u].append(v)
  a[v].append(u)

def dfsDef(x):
  visitList[x] = True
  for i in a[x]:
    if not visitList[i]:
      dfsDef(i)

for i in range(1, n + 1):
  if not visitList[i]:
    answer += 1
    dfsDef(i)

print(answer)