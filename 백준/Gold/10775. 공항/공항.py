import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
parent = [i for i in range(g + 1)]
airplane = []
cnt = 0

for _ in range(p):
  airplane.append(int(input()))

def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

for ap in airplane:
  x = find(ap)
  if x == 0:
    break
  union(x, x - 1)
  cnt += 1

print(cnt)