import sys
input = sys.stdin.readline

while True:
  numList = str(input().strip())
  isPalindrome = True
  if numList == '0':
    break
  for i in range(len(numList) // 2):
    if numList[i] != numList[-(i + 1)]:
      isPalindrome = False
      break

  if isPalindrome:
    print("yes")
  else:
    print("no")