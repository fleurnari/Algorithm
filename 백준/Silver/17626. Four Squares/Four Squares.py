import sys
input = sys.stdin.readline
n = int(input())
dpTable = [0, 1]

for i in range(2, n + 1):
  num = i
  for j in range(1, i):
    if j ** 2 > i:
      break
    num = min(num, dpTable[i - j ** 2])
  dpTable.append(num + 1)

print(dpTable[-1])