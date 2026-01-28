import sys
input = sys.stdin.readline
n = int(input())

def to_nbinary(n):
  if n == 0:
    return '0'
  result = []
  while n != 0:
    r = n % 2
    result.append(str(r))
    n = (n - r) // -2
  return ''.join(result[::-1])

print(to_nbinary(n))