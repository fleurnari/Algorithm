import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))
graph = [[sys.maxsize] * (n + 1) for _ in range(n+ 1)]
result = 0

for _ in range(1, r + 1):
  a, b, l = map(int, input().split())
  graph[a][b] = l
  graph[b][a] = l

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n + 1):
  tmp = 0
  for j in range(1, n + 1):
    if graph[i][j] <= m:
      tmp += t[j]
  result = max(result, tmp)

print(result)