import sys
input = sys.stdin.readline
t = int(input())
dpTable = [0] * 12
dpTable[1] = 1
dpTable[2] = 2
dpTable[3] = 4

for i in range(4, 12):
  dpTable[i] = dpTable[i - 1] + dpTable[i - 2] + dpTable[i - 3]
  

for i in range(t):
  n = int(input())
  print(dpTable[n])