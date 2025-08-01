import sys
input = sys.stdin.readline
melodyList = list(map(int, input().split()))

if melodyList[0] == 1:
  for i in range(1, 8):
    if melodyList[i] != i + 1:
      print("mixed")
      break
    if i == 7:
      print("ascending")
elif melodyList[0] == 8:
  for i in range(1, 8):
    if melodyList[i] != 8 - i:
      print("mixed")
      break
    if i == 7:
      print("descending")
else:
  print("mixed")