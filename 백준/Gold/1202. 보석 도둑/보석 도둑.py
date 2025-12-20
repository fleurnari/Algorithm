import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
jewel = [[*map(int, input().split())] for _ in range(n)]
bag = [int(input()) for _ in range(k)]
jewel.sort()
bag.sort()
tmp = []
result = 0

for b in bag:
  while jewel and jewel[0][0] <= b:
    heapq.heappush(tmp, -jewel[0][1])
    heapq.heappop(jewel)
  if tmp:
    result -= heapq.heappop(tmp)

print(result)