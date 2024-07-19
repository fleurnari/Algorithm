from collections import deque

n = int(input())

arr = [[] for i in range(n + 1)]

distList = [0] * (n + 1)

visitList = [False] * (n + 1)

for i in range(n):
  data = list(map(int, input().split()))
  idx = 0
  start = data[idx]
  idx += 1
  while True:
    if data[idx] == -1:
      break
    end = data[idx]
    dist = data[idx + 1]
    arr[start].append((end, dist))
    idx += 2

def bfs(v):
  q = deque()
  q.append(v)
  visitList[v] = True

  while q:
    now = q.popleft()
    for i in arr[now]:
      if not visitList[i[0]]:
        q.append(i[0])
        visitList[i[0]] = True
        distList[i[0]] = distList[now] + i[1]


bfs(1)
max = 1

for i in range(2, n + 1):
  if distList[max] < distList[i]:
    max = i

distList = [0] * (n + 1)

visitList = [False] * (n + 1)

bfs(max)

distList.sort()

print(distList[n])