import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for i in range(t):
  p = input().rstrip()
  n = int(input())
  x = input().rstrip()[1:-1].split(',')
  queue = deque(x)
  flag = 0
  
  if n == 0:
    queue = []
  
  for j in p:
    if j == 'R':
      flag += 1
    elif j == 'D':
      if len(queue) == 0:
        print('error')
        break
      else:
        if flag % 2 == 0:
          queue.popleft()
        else:
          queue.pop()
  else:
    if flag % 2 == 0:
      print("[" + ",".join(queue) + "]")
    else:
      queue.reverse()
      print("[" + ",".join(queue) + "]")