from queue import PriorityQueue

import sys

input = sys.stdin.readline

print = sys.stdout.write

n = int(input())

pq = PriorityQueue()


for i in range(n):
  num = int(input())

  if num == 0:
    if pq.empty():
      print("0\n")

    else:
      front = pq.get()
      print(str(front[1]) + "\n")

  else:
    pq.put((abs(num), num))
