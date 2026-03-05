import sys
from bisect import bisect_left
input = sys.stdin.readline
t = int(input())

for _ in range(t):
   n, m = map(int, input().split())
   a = list(map(int, input().split()))
   b = list(map(int, input().split()))
   b.sort()
   answer = 0
   for num in a:
      answer += bisect_left(b, num)
   print(answer)