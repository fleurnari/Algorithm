import sys
input = sys.stdin.readline
numList = []
answer = 0

for i in range(10):
  numList.append(int(input()) % 42)

for i in range(len(numList)):
  if numList[i] not in numList[0:i]:
    answer += 1

print(answer)