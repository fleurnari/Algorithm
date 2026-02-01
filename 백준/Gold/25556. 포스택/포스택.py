import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
stack = []

for x in a:
  idx = -1
  maxTop = -1
  
  for i in range(len(stack)):
    if stack[i][-1] < x and stack[i][-1] > maxTop:
      idx = i
      maxTop = stack[i][-1]

  if idx != -1:
    stack[idx].append(x)
  else:
    if len(stack) < 4:
      stack.append([x])
    else:
      print("NO")
      exit()

print("YES")