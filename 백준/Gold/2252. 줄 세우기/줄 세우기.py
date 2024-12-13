from collections import deque
n, m = map(int, input().split())
stdList = [[] for i in range(n + 1)]
stdChk = [0] * (n + 1)

for i in range(m):
  s, e = map(int, input().split())
  stdList[s].append(e)
  stdChk[e] += 1

queue = deque()

for i in range(1, n + 1):
  if stdChk[i] == 0:
    queue.append(i)

while queue:
  now = queue.popleft()
  print(now, end = ' ')
  for i in stdList[now]:
    stdChk[i] -= 1
    if stdChk[i] == 0:
      queue.append(i)