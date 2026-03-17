import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    data = list(map(int, input().split()))

    if data[0] == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
    else:
        for x in data[1:]:
            heapq.heappush(heap, -x)