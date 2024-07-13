import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())


def findPrime(num):
  for i in range(2, int(num / 2 + 1)):
    if num % i == 0:
      return False
  return True


def dfsDef(num):
  if len(str(num)) == n:
    print(num)
  else:
    for i in range(1, 10):
      if i % 2 == 0:
        continue
      else:
        if findPrime(num * 10 + i):
          dfsDef(num * 10 + i)

dfsDef(2)
dfsDef(3)
dfsDef(5)
dfsDef(7)