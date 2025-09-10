import sys
input = sys.stdin.readline
strExp = list(map(str, input().split("-")))
result = 0

def calc(exp):
  sum = 0
  expression = str(exp).split("+")
  for i in expression:
    sum += int(i)
  return sum

for i in range(len(strExp)):
  tmp = calc(strExp[i])
  if i == 0:
    result += tmp
  else:
    result -= tmp

print(result)