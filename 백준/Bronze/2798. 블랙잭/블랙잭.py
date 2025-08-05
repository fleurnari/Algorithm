import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numList = list(map(int, input().split()))
sum = 0

for i in range(len(numList) - 2):
  for j in range(i + 1, len(numList) - 1):
    for k in range(j + 1, len(numList)):
      tmp = numList[i] + numList[j] + numList[k]
      if tmp <= m:
        if tmp == m:
          print(tmp)
          exit()
        elif sum < tmp:
          sum = tmp
        else:
          continue

print(sum)