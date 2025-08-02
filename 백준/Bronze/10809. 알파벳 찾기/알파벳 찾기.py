import sys
input = sys.stdin.readline
s = str(input().strip())
answerList = [0] * 26

for i in range(len(answerList)):
  if chr(97 + i) in s:
    answerList[i] = s.index(chr(97 + i))
  else:
    answerList[i] = -1
  print(answerList[i], end=' ')