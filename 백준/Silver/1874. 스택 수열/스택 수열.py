import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * n
stack = []
num = 1
result = True
answer = ""

for i in range(n):
  arr[i] = int(input())

for i in range(n):
  now = arr[i]
  if now >= num:
    while now >= num:
      stack.append(num)
      num += 1
      answer += "+\n"
    stack.pop()
    answer += "-\n"
  else:
    popNum = stack.pop()
    if popNum > now:
      print("NO")
      result = False
      break
    else:
      answer += "-\n"

if result == True:
  print(answer)
