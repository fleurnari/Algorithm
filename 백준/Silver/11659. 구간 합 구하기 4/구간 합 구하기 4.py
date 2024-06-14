import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

sumArr = [0]

tmp = 0

for i in numbers:
  tmp += i
  sumArr.append(tmp)

for i in range(m):
  start, end = map(int, input().split())
  print(sumArr[end] - sumArr[start - 1])