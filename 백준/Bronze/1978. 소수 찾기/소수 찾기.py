import sys
input = sys.stdin.readline
n = int(input())
numList = list(map(int, input().split()))
answer = 0

for i in range(len(numList)):
  isPrime = True
  if numList[i] == 1:
    isPrime = False
  elif numList[i] == 2:
    isPrime = True
  else:
    for j in range(2, numList[i]):
      if numList[i] % j == 0:
        isPrime = False
        break
  if isPrime:
    answer += 1

print(answer)