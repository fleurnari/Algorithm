import sys
input = sys.stdin.readline
sYear = int(input())

if (sYear % 4 == 0 and sYear % 100 != 0) or sYear % 400 == 0:
  print(1)
else:
  print(0)