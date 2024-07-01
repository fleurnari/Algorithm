import sys

input = sys.stdin.readline

n = int(input())

a = []

for i in range(n):
  a.append((int(input()), i))

maxNum = 0
sortA = sorted(a)

for i in range(n):
  if maxNum < sortA[i][1] - i:
    maxNum = sortA[i][1] - i

print(maxNum + 1)