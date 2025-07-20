import sys
input = sys.stdin.readline
iScore = int(input())

if iScore in range(90, 101):
  print("A")
elif iScore in range(80, 90):
  print("B")
elif iScore in range(70, 80):
  print("C")
elif iScore in range(60, 70):
  print("D")
else:
  print("F")
