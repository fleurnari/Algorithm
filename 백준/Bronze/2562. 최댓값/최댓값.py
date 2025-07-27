import sys
input = sys.stdin.readline
nList = [0] * 9
maxNum = 0
maxIdx = 0

for i in range(9):
  nList[i] = int(input())
  if maxNum < nList[i]:
    maxNum = nList[i]
    maxIdx = i + 1

print(maxNum)
print(maxIdx)