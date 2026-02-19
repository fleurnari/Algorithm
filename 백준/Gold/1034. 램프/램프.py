import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
lamp = [input().strip() for _ in range(n)]
k = int(input())
counter = Counter(lamp)
answer = 0

for row in counter:
  zero = row.count('0')
  if zero <= k and (k - zero) % 2 == 0:
    answer = max(answer, counter[row])

print(answer)