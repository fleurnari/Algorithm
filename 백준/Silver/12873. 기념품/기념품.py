import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque(range(1, n + 1))
i = 1

while len(queue) > 1:
  k = (i ** 3 - 1) % len(queue)
  queue.rotate(-k)
  queue.popleft()
  i += 1

print(queue[0])