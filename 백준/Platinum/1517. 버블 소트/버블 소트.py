import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

a.insert(0, 0)

tmp = [0] * int(n + 1)

answer = 0



def sortDef(start, end):
  global answer
  
  if end - start < 1:
    return

  mid = int(start + (end - start) / 2)

  sortDef(start, mid)
  sortDef(mid + 1, end)

  for i in range(start, end + 1):
    tmp[i] = a[i]

  k = start
  idx1 = start
  idx2 = mid + 1

  while idx1 <= mid and idx2 <= end:
    if tmp[idx1] > tmp[idx2]:
      a[k] = tmp[idx2]
      answer += (idx2 - k)
      k += 1
      idx2 += 1
    else:
      a[k] = tmp[idx1]
      k += 1
      idx1 += 1

  while idx1 <= mid:
    a[k] = tmp[idx1]
    k += 1
    idx1 += 1

  while idx2 <= end:
    a[k] = tmp[idx2]
    k += 1
    idx2 += 1
      
sortDef(1, n)

print(answer)