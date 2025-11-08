import sys
input = sys.stdin.readline
str = input().strip()
expStr = input().strip()
stack = []

for i in range(len(str)):
  stack.append(str[i])
  if len(stack) >= len(expStr):
    while stack[-len(expStr):] == list(expStr):
      for _ in range(len(expStr)):
        stack.pop()

if len(stack) == 0:
  print("FRULA")
else:
  print("".join(stack))