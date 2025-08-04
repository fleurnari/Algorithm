import sys
input = sys.stdin.readline
n = int(input())
cnt = 0

for i in range(n):
  sum = 0
  for j in range(len(str(i))):
    sum += int(str(i)[j])
  sum += i
  if sum == n:
    print(i)
    cnt += 1
    break

if cnt == 0:
  print(0)