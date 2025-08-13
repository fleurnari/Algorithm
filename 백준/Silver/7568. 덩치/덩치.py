import sys
input = sys.stdin.readline
n = int(input())
peopleList = []
answerList = [1] * n

for i in range(n):
  x, y = map(int, input().split())
  peopleList.append([x, y])

for i in range(len(peopleList)):
  for j in range(len(peopleList)):
    if peopleList[i][0] < peopleList[j][0] and peopleList[i][1] < peopleList[j][1]:
      answerList[i] += 1

for i in range(len(answerList)):
  print(answerList[i], end = ' ')