from queue import PriorityQueue

n = int(input())

plus = PriorityQueue()

minus = PriorityQueue()

one = 0

zero = 0

answer = 0

for i in range(n):
  num = int(input())
  if num > 1:
    plus.put(num * -1)
  elif num == 1:
    one += 1
  elif num == 0:
    zero += 1
  else:
    minus.put(num)

while plus.qsize() > 1:
  a = plus.get() * -1
  b = plus.get() * -1
  answer += a * b

if plus.qsize() > 0:
  answer += plus.get() * -1

while minus.qsize() > 1:
  a = minus.get()
  b = minus.get()
  answer += a * b

if minus.qsize() > 0:
  if zero == 0:
    answer += minus.get()

answer += one

print(answer)