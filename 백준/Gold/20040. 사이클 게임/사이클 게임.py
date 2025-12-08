import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
end = 0

def find(x):
  if x == parent[x]:
    return x
  else:
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y, idx):
  global end
  x = find(x)
  y = find(y)
  if x != y:
    parent[max(x, y)] = min(x, y)
  elif end == 0:
    end = idx

for i in range(m):
  a, b = map(int, input().split())
  union(a, b, i + 1)

print(end)