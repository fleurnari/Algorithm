import sys
input = sys.stdin.readline
n = int(input())
parentList = [-1] * 3001

def ccw(x1, y1, x2, y2, x3, y3):
  tmp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
  if tmp > 0:
    return 1
  elif tmp == 0:
    return 0
  else:
    return -1

def chkOverlab(x1, y1, x2, y2, x3, y3, x4, y4):
  if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) \
  and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
    return True
  else:
    return False

def chkCross(x1, y1, x2, y2, x3, y3, x4, y4):
  abc = ccw(x1, y1, x2, y2, x3, y3)
  abd = ccw(x1, y1, x2, y2, x4, y4)
  cda = ccw(x3, y3, x4, y4, x1, y1)
  cdb = ccw(x3, y3, x4, y4, x2, y2)

  if abc * abd == 0 and cda * cdb == 0:
    return chkOverlab(x1, y1, x2, y2, x3, y3, x4, y4)
  elif abc * abd <= 0 and cda * cdb <= 0:
    return True
  else:
    return False

def find(a):
  if parentList[a] < 0:
    return a
  else:
    parentList[a] = find(parentList[a])
    return parentList[a]

def union(a, b):
  p = find(a)
  q = find(b)
  if p == q:
    return
  parentList[p] += parentList[q]
  parentList[q] = p

inputList = []
inputList.append([])

for i in range(1, n + 1):
  inputList.append([])
  inputList[i] = list(map(int, input().split()))
  for j in range(1, i):
    if chkCross(inputList[i][0], inputList[i][1], inputList[i][2], inputList[i][3], inputList[j][0], inputList[j][1], inputList[j][2], inputList[j][3]):
      union(i, j)

result1 = 0
result2 = 0

for i in range(1, n + 1):
  if parentList[i] < 0:
    result1 += 1
    result2 = min(result2, parentList[i])

print(result1)
print(result2 * -1)