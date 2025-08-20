import sys
input = sys.stdin.readline
n = int(input())
levelList = []

def newRound(value):
  return int(value) + 1 if value - int(value) >= 0.5 else int(value) 

for i in range(n):
  levelList.append(int(input()))
levelList.sort()

if n == 0:
  print(0)
else:
  removeLevel = newRound(n * 0.15)
  if removeLevel != 0:
    levelList = levelList[removeLevel : n - removeLevel]
  print(newRound(sum(levelList) / len(levelList)))