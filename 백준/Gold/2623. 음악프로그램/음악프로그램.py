import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
queue, answer = [], []

for _ in range(m):
  arr = list(map(int, input().split()))
  for i in range(1, arr[0]):
    graph[arr[i]].append(arr[i + 1])
    indegree[arr[i + 1]] += 1

for i in range(1, n + 1):
  if indegree[i] == 0:
    queue.append(i)

while queue:
  now = queue.pop(0)
  answer.append(now)
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      queue.append(i)

if len(answer) != n:
  print(0)
else:
  for i in answer:
    print(i)