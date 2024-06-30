n = int(input())

answer = [0] * n


for i in range(n):
  answer[i] = int(input())

for i in range(n - 1):
  for j in range(n - 1 - i):
    if answer[j] > answer[j + 1]:
      tmp = answer[j]
      answer[j] = answer[j + 1]
      answer[j + 1] = tmp

for i in range(n):
  print(answer[i])