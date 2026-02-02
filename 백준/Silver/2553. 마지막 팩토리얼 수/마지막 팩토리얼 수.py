import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
def factorial(x):
  if x == 0:
    return 1
  else:
    return x * factorial(x - 1)

fac = str(factorial(n))
for i in range(len(fac) - 1, -1, -1):
  if fac[i] != '0':
    print(fac[i])
    break