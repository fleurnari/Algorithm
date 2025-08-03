import sys
input = sys.stdin.readline

while True:
  inputList = list(map(int, input().split()))
  inputList.sort()
  if inputList[0] == 0 and inputList[1] == 0 and inputList[2] == 0:
    break
  print("right" if inputList[0] ** 2 + inputList[1] ** 2 == inputList[2] ** 2 else "wrong")