import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
a, b = map(int, input().split())

def sumX(x):
  if x <= 0:
    return 0

  power = int(math.log2(x))
  x2power = 2 ** power
  if x2power == x:
    return power * x // 2 + 1
  diff = x - x2power
  return sumX(x2power) + diff + sumX(diff)

print(sumX(b) - sumX(a - 1))