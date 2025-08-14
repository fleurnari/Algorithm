import sys
input = sys.stdin.readline
n = int(input())
cdnList = []

for i in range(n):
  x, y = map(int, input().split())
  cdnList.append([x, y])

cdnList.sort(key=lambda x: (x[0], x[1]))

for i in range(len(cdnList)):
  print(cdnList[i][0], cdnList[i][1])