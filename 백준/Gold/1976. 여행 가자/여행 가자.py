n = int(input())
m = int(input())

rep = [0] * (n + 1)

for i in range(1, n + 1):
  rep[i] = i

city = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
  city[i] = list(map(int, input().split()))
  city[i].insert(0, 0)

route = list(map(int, input().split()))
route.insert(0, 0)

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

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if city[i][j] == 1:
      union(i, j)

idx = find(route[1])
bConnect = True

for i in range(2, len(route)):
  if idx != find(route[i]):
    bConnect = False
    break

if bConnect:
  print("YES")
else:
  print("NO")