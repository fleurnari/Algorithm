import sys
input = sys.stdin.readline
dpTable = [0] * 51
probTable = [0] * 51
m = int(input())
stoneList = list(map(int, input().split()))
k = int(input())
totalCnt = 0
result = 0

for i in range(m):
  totalCnt += stoneList[i]

for i in range(m):
  if stoneList[i] >= k:
    probTable[i] = 1
    for j in range(k):
      probTable[i] = probTable[i] * (stoneList[i] - j) / (totalCnt - j)
    result += probTable[i]

print(result)