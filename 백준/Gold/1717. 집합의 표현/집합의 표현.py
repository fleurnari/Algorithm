import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
rep = [0] * (n + 1)

for i in range(0, n + 1):
  rep[i] = i

def find(a):
  if a == rep[a]:
    return a
  else:
    rep[a] = find(rep[a])
    return rep[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    rep[b] = a

def chkSame(a, b):
  a = find(a)
  b = find(b)
  if a == b:
    return True
  else:
    return False

for i in range(m):
  query, a, b = map(int, input().split())
  if query == 0:
    union(a, b)
  else:
    if chkSame(a, b):
      print("YES")
    else:
      print("NO")