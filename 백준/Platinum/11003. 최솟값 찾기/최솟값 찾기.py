from collections import deque

n, l = map(int, input().split())

a = list(map(int, input().split()))

d = deque()

for i in range(n):
  
  while d and d[-1][0] > a[i]:
    d.pop()
  d.append((a[i], i))
  
  if d[0][1] <= i - l:
    d.popleft()

  print(d[0][0], end=' ')