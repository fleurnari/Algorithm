import sys
input = sys.stdin.readline
n = int(input())
sizeArr = list(map(int, input().split()))
tCnt = [0] * len(sizeArr)
t, p = map(int, input().split())
pSet, pCnt = 0, 0

for i in range(len(sizeArr)):
  if sizeArr[i] == 0:
    tCnt[i] = 0
  elif sizeArr[i] <= t:
    tCnt[i] = 1
  elif sizeArr[i] % t == 0:
    tCnt[i] = sizeArr[i] // t
  else:
    tCnt[i] = sizeArr[i] // t + 1

pSet = n // p
pCnt = n % p

print(sum(tCnt))
print(pSet, pCnt)