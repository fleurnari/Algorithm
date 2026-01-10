import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
line = [tuple(map(int, input().split())) for _ in range(n)]
line.sort()
lis = []
lisIdx = []
prev = [-1] * n

for i, l in enumerate(line):
  a, b = l
  idx = bisect_left(lis, b)
  if idx >= len(lis):
    lis.append(b)
    lisIdx.append(i)
  else:
    lis[idx] = b
    lisIdx[idx] = i
  prev[i] = -1 if idx == 0 else lisIdx[idx - 1]

lisLine = []
current = lisIdx[-1]
while current != -1:
  lisLine.append(current)
  current = prev[current]

answer = [line[i][0] for i in range(n) if i not in set(lisLine)]

print(len(answer))
for a in answer:
  print(a)