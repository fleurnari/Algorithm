import sys
input = sys.stdin.readline
m = 0

for i in range(3, 0, -1):
  n = input().strip()
  if n not in ['Fizz', 'Buzz', 'FizzBuzz']:
    m = int(n) + i
if m % 3 == 0 and m % 5 == 0:
  print('FizzBuzz')
elif m % 3 == 0 and m % 5 != 0 :
  print('Fizz')
elif m % 3 != 0 and m % 5 == 0 :
  print('Buzz')
else:
  print(m)