import sys
input = sys.stdin.readline
n = int(input())
peopleList = []

for i in range(n):
  x, y = map(str, input().split())
  peopleList.append([int(x), y])

peopleList.sort(key=lambda x: x[0])

for i in range(len(peopleList)):
  print(peopleList[i][0], peopleList[i][1])
