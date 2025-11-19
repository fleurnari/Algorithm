import sys
input = sys.stdin.readline
tc = int(input())

def bellmanford():
  for i in range(n):
    for j in range(len(edges)):
      now, next, cost = edges[j]
      if dist[next] > dist[now] + cost:
        dist[next] = dist[now] + cost
        if i == n - 1:
          return True
  return False
        

for _ in range(tc):
  n, m, w = map(int, input().split())
  edges = []
  dist = [sys.maxsize] * (n + 1)
  for i in range(m + w):
    s, e, t = map(int, input().split())
    if i >= m:
      t = -t
    else:
      edges.append((e, s, t))
    edges.append((s, e, t))
  if bellmanford():
    print("YES")
  else:
    print("NO")