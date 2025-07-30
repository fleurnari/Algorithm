import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
sNum = str(a * b * c)

for i in range(10):
  print(sNum.count(str(i)))
