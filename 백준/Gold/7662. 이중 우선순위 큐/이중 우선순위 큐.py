import sys
import heapq
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  k = int(input())
  maxHeap, minHeap = [], []
  dic = {}
  for _ in range(k):
    c, n = input().strip().split()
    if c == 'I':
      heapq.heappush(maxHeap, -int(n))
      heapq.heappush(minHeap, int(n))
      if int(n) in dic.keys():
        dic[int(n)] += 1
      else:
        dic[int(n)] = 1
    else:
      if int(n) == 1:
        while True:
          if maxHeap:
            if dic[-maxHeap[0]] == 0:
              heapq.heappop(maxHeap)
            else:
              break
          else:
            break
        if maxHeap:
          dic[-heapq.heappop(maxHeap)] -= 1
      else:
        while True:
          if minHeap:
            if dic[minHeap[0]] == 0:
              heapq.heappop(minHeap)
            else:
              break
          else:
            break
        if minHeap:
          dic[heapq.heappop(minHeap)] -= 1

  while True:
    if maxHeap:
      if dic[-maxHeap[0]] == 0:
        heapq.heappop(maxHeap)
      else:
        break
    else:
      break

  while True:
    if minHeap:
      if dic[minHeap[0]] == 0:
        heapq.heappop(minHeap)
      else:
        break
    else:
      break

  if minHeap:
    max = -heapq.heappop(maxHeap)
    min = heapq.heappop(minHeap)
    print(max, min)
  else:
    print('EMPTY')