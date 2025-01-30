import sys
input = sys.stdin.readline

fctList = [0] * 21
pList = [0] * 21
visitList = [False] * 21
n = int(input())
fctList[0] = 1

for i in range(1, n + 1):
  fctList[i] = fctList[i - 1] * i

inputList = list(map(int, input().split()))

if inputList[0] == 1:
  k = inputList[1]
  for i in range(1, n + 1):
    cnt = 1
    for j in range(1, n + 1):
      if visitList[j]:
        continue
      if k <= cnt * fctList[n - i]:
        k -= (cnt - 1) * fctList[n - i]
        pList[i] = j
        visitList[j] = True
        break
      cnt += 1
  for i in range(1, n + 1):
    print(pList[i], end = ' ')
else:
  k = 1
  for i in range(1, n + 1):
    cnt = 0
    for j in range(1, inputList[i]):
      if not visitList[j]:
        cnt += 1
    k += cnt * fctList[n - i]
    visitList[inputList[i]] = True
  print(k)

