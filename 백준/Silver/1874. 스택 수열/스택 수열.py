n = int(input())

seqArr = [0] * n

for i in range(n):
    seqArr[i] = int(input())

stack = []

num = 1

answer = ""

result = True


for i in range(n):
  seq = seqArr[i]

  if num <= seq:
    while num <= seq:
      stack.append(num)
      num += 1
      answer += "+\n"

    stack.pop()
    answer += "-\n"

  else:
    popNum = stack.pop()

    if seq < popNum:
      print("NO")
      result = False
      break
    else:
      answer += "-\n"

if result is True:
  print(answer)