import sys
input = sys.stdin.readline
n = int(input())
nList = list(map(int, input().split()))
maxNum = nList[0]
minNum = nList[0]

for i in range(1, len(nList)):
  if maxNum < nList[i]:
    maxNum = nList[i]
  if minNum > nList[i]:
    minNum = nList[i]

print(minNum, maxNum)