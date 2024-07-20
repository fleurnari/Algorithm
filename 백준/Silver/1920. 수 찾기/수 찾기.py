n = int(input())

arr = list(map(int, input().split()))

arr.sort()

m = int(input())

searchArr = list(map(int, input().split()))

for i in range(m):
  exist = False
  searchNum = searchArr[i]

  start = 0
  end = len(arr) - 1

  while start <= end:
    mIdx = int((start + end) / 2)
    mNum = arr[mIdx]

    if mNum < searchNum:
      start = mIdx + 1
    elif mNum > searchNum:
      end = mIdx - 1
    else:
      exist = True
      break

  if exist:
    print(1)
  else:
    print(0)
