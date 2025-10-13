import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dpTable = [1] * n

for i in range(1, n):
  for j in range(i):
    if arr[i] > arr[j]:
      dpTable[i] = max(dpTable[i], dpTable[j] + 1)

print(max(dpTable))