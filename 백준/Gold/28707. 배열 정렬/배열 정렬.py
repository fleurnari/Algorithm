import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
a = ''
for i in map(int, input().split()):
  a += str(i - 1)
answer = ''.join(sorted(a))
m = int(input())
commandList = [list(map(int, input().split())) for _ in range(m)]
costList = defaultdict()
costList[a] = 0
queue = [(0, a)]

while queue:
  cost, current = heappop(queue)
  if costList[current] > cost:
    continue
  if current == answer:
    continue
  for l, r, c in commandList:
    next = current[:l - 1] + current[r - 1] + current[l:r - 1] + current[l - 1] + current[r:]
    if next in costList and costList[next] <= cost + c:
      continue
    costList[next] = cost + c
    heappush(queue, (cost + c, next))

if answer in costList:
  print(costList[answer])
else:
  print(-1)