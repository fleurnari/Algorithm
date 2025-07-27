import sys
input = sys.stdin.readline

n = int(input())
nList = list(input().strip())
sum = 0

for i in range(len(nList)):
  sum += int(nList[i])

print(sum)