import sys
input = sys.stdin.readline
n = int(input())
nList = list(map(int, input().split()))
nList.sort()
m = int(input())
mList = list(map(int, input().split()))

for i in range(len(mList)):
    isFind = False
    findValue = mList[i]
    s = 0
    e = len(nList) - 1
    while s <= e:
      midIdx = (s + e) // 2
      midValue = nList[midIdx]
      if midValue == findValue:
        isFind = True
        break
      elif midValue > findValue:
        e = midIdx - 1
      else:
        s = midIdx + 1
    if isFind:
      print(1)
    else:
      print(0)