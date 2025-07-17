import sys
input = sys.stdin.readline
numList = list(map(int, input().split()))
sum = 0

for i in range(0, len(numList)):
  sum += numList[i] * numList[i]

print(sum % 10)