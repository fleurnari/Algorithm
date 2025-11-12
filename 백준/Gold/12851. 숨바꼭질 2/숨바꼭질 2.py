import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
max = 10 ** 5
visitList = [-1] * (max + 1)
visitList[n] = 0
cnt = 0

queue = deque()
queue.append(n)

while queue:
  current = queue.popleft()
  if current == k:
    cnt += 1
  for i in (current * 2, current - 1, current + 1):
    if 0 <= i <= max:
      if visitList[i] == -1 or visitList[i] >= visitList[current] + 1:
        visitList[i] = visitList[current] + 1
        queue.append(i)

print(visitList[k])
print(cnt)