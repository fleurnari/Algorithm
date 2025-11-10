import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
answer = 0
dpTable1 = [1] * n
dpTable2 = [1] * n

for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      dpTable1[i] = max(dpTable1[i], dpTable1[j] + 1)

for i in range(n)[::-1]:
  for j in range(i, n):
    if a[i] > a[j]:
      dpTable2[i] = max(dpTable2[i], dpTable2[j] + 1)

for i in range(n):
  answer = max(answer, dpTable1[i] + dpTable2[i])

print(answer - 1)