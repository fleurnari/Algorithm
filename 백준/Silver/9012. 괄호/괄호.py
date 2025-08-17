import sys
input = sys.stdin.readline
print = sys.stdout.write
t = int(input())
stack = []

for i in range(t):
  inputStr = input()
  for j in range(len(inputStr)):
    if inputStr[j] == '(':
      stack.append(inputStr[j])
    elif inputStr[j] == ')':
      if len(stack) != 0:
        stack.pop()
      else:
        print("NO\n")
        break
    if j == len(inputStr) - 1:
      if len(stack) == 0:
        print("YES\n")
      else:
        print("NO\n")
        stack = []
        break