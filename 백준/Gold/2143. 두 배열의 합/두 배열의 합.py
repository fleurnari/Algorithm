import sys
import bisect
input = sys.stdin.readline
t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
asum, bsum = [], []
answer = 0

for i in range(n):
  for j in range(i + 1, n + 1):
    asum.append(sum(a[i:j]))

for i in range(m):
  for j in range(i + 1, m + 1):
    bsum.append(sum(b[i:j]))

asum.sort()
bsum.sort()

for i in range(len(asum)):
  tmp = t - asum[i]
  left = bisect.bisect_left(bsum, tmp)
  right = bisect.bisect_right(bsum, tmp)
  answer += (right - left)

print(answer)