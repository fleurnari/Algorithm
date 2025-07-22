import sys
input = sys.stdin.readline
n, x = map(int, input().split())
numList = list(map(int, input().split()))
answerList = []

for i in range(len(numList)):
  if numList[i] < x:
    answerList.append(numList[i])

for i in range(len(answerList)):
  print(answerList[i], end = ' ')