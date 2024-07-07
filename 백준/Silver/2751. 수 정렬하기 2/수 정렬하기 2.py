import sys

input = sys.stdin.readline

print = sys.stdout.write

n = int(input())

sortArr = [0] * int(n + 1)

tmpArr = [0] * int(n + 1)

for i in range(1, n + 1):
  sortArr[i] = int(input())


def sortDef(start, end):
  if end - start < 1:
    return
    
  mid = int(start + (end - start) / 2)

  sortDef(start, mid)
  sortDef(mid + 1, end)

  for i in range(start, end + 1):
    tmpArr[i] = sortArr[i]

  k = start
  idx1 = start
  idx2 = mid + 1

  while idx1 <= mid and idx2 <= end:
    if tmpArr[idx1] > tmpArr[idx2]:
      sortArr[k] = tmpArr[idx2]
      k += 1
      idx2 += 1
    else:
      sortArr[k] = tmpArr[idx1]
      k += 1
      idx1 += 1

  while idx1 <= mid:
    sortArr[k] = tmpArr[idx1]
    k += 1
    idx1 += 1
  while idx2 <= end:
    sortArr[k] = tmpArr[idx2]
    k += 1
    idx2 += 1


sortDef(1, n)

for i in range(1, n + 1):
  print(str(sortArr[i]) + "\n")