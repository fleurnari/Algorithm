import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
sumArr = [0]

for i in arr:
  sum += i
  sumArr.append(sum)

for i in range(m):
  a, b = map(int, input().split())
  print(sumArr[b] - sumArr[a - 1])