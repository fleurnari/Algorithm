import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  answerList = list(str(input()))
  scoreList = [0] * len(answerList)
  for i in range(len(answerList)):
    if answerList[i] == 'O':
      if i == 0:
        scoreList[i] = 1
      else:
        scoreList[i] = scoreList[i - 1] + 1
    else:
      scoreList[i] = 0
  print(sum(scoreList))