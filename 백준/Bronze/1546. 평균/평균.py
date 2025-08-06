import sys
input = sys.stdin.readline
n = int(input())
scoreList = list(map(int, input().split()))
maxScore = 0
sum = 0

for i in range(len(scoreList)):
  sum += scoreList[i]
  if maxScore < scoreList[i]:
    maxScore = scoreList[i]

print(sum / maxScore / n * 100)