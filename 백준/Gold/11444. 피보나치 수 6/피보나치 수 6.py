import sys
from functools import cache
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

@cache
def fib(n):
  if n <= 2:
    return 1
  elif n % 2 == 0:
    return (fib(n // 2) * (2 * fib(n // 2 - 1) + fib(n // 2))) % 1000000007
  else:
    return (fib(n // 2 + 1) ** 2 + fib(n // 2) ** 2) % 1000000007

print(fib(n))