import sys
input = sys.stdin.readline
isbn = input().strip()
answer = 0
isEven = False

for i in range(len(isbn)):
  if isbn[i] == '*':
    if i % 2 != 0 :
      isEven = True
    continue
  answer += int(isbn[i]) * (1 if i % 2 == 0 else 3)

if isEven:
  for i in range(10):
    if (answer + (i * 3)) % 10 == 0:
      print(i)
      break
else:
  print(10 - (answer % 10))