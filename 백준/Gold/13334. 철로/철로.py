import sys
import heapq
input = sys.stdin.readline
n = int(input())
location = []
heap = []
answer = 0

for _ in range(n):
  h, o = map(int, input().split())
  location.append((min(h, o), max(h, o)))
    
location.sort(key=lambda x: (x[1], x[0]))
d = int(input())

for lc in location:
  start, end = lc
  heapq.heappush(heap, start)
  startPoint = end - d
  while heap and heap[0] < startPoint:
    heapq.heappop(heap)
  answer = max(answer, len(heap))

print(answer)