import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
inputList1 = list(input())
inputList2 = list(input())
inputList1.pop()
inputList2.pop()
dpTable = [[0 for j in range(len(inputList2) + 1)] for i in range(len(inputList1) + 1)]
lcsList = []

for i in range(1, len(inputList1) + 1):
  for j in range(1, len(inputList2) + 1):
    if inputList1[i - 1] == inputList2[j - 1]:
      dpTable[i][j] = dpTable[i - 1][j - 1] + 1
    else:
      dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])

print(dpTable[len(inputList1)][len(inputList2)])

def setLcsList(row, col):
  if row == 0 or col == 0:
    return
  if inputList1[row - 1] == inputList2[col - 1]:
    lcsList.append(inputList1[row - 1])
    setLcsList(row - 1, col - 1)
  else:
    if dpTable[row - 1][col] > dpTable[row][col - 1]:
      setLcsList(row - 1, col)
    else:
      setLcsList(row, col - 1)

setLcsList(len(inputList1), len(inputList2))

for i in range(len(lcsList) - 1, -1, -1):
  print(lcsList.pop(i), end = '')

print()