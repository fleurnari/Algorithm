import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
q = deque()
answer = []

for i in range(n):
  q.append(i + 1)

for i in range(n):
  for j in range(k - 1):
    tmp = q.popleft()
    q.append(tmp)
  answer.append(q.popleft())
    

print("<", end="")
for i in range(len(answer) - 1):
  print(answer[i], end=", ")
print(answer[-1], end="")
print(">", end="")