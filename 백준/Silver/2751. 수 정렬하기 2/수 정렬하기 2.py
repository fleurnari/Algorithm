import sys
input = sys.stdin.readline
print = sys.stdout.write

def mergeSort(s, e):
  if e - s < 1:
    return
    
  m = int(s + (e - s) / 2)
  mergeSort(s, m)
  mergeSort(m + 1, e)
  
  for i in range(s, e + 1):
    tmp[i] = numList[i]
    
  k = s
  idx1 = s
  idx2 = m + 1
  
  while idx1 <= m and idx2 <= e:
    if tmp[idx1] > tmp[idx2]:
      numList[k] = tmp[idx2]
      k += 1
      idx2 += 1
    else:
      numList[k] = tmp[idx1]
      k += 1
      idx1 += 1
      
  while idx1 <= m:
    numList[k] = tmp[idx1]
    k += 1
    idx1 += 1

  while idx2 <= e:
    numList[k] = tmp[idx2]
    k += 1
    idx2 += 1
    

n = int(input())
numList = [0] * int(n + 1)
tmp = [0] * int(n + 1)

for i in range(1, n + 1):
  numList[i] = int(input())

mergeSort(1, n)

for i in range(1, n + 1):
  print(str(numList[i]) + '\n')