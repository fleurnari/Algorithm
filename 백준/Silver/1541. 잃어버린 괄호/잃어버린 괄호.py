a = list(map(str, input().split("-")))

answer = 0

def sumDef(i):
  tmp = str(i).split("+")
  sum = 0
  for i in tmp:
    sum += int(i)
  return sum

for i in range(len(a)):
  tmp = sumDef(a[i])
  if i == 0:
    answer += tmp
  else:
    answer -= tmp

print(answer)