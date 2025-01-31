import sys
input = sys.stdin.readline

n = int(input())
inputList = list(map(int, input().split()))
leftTable = [0] * n
rightTable = [0] * n
leftTable[0] = inputList[0]
rightTable[n - 1] = inputList[n - 1]
result = leftTable[0]

for i in range(1, n):
  leftTable[i] = max(inputList[i], leftTable[i - 1] + inputList[i])
  result = max(result, leftTable[i])

for i in range(n - 2, -1, -1):
  rightTable[i] = max(inputList[i], rightTable[i + 1] + inputList[i])

for i in range(1, n - 1):
  tmp = leftTable[i - 1] + rightTable[i + 1]
  result = max(result, tmp)

print(result)