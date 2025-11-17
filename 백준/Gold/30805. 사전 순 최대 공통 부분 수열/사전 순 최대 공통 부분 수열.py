import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
result = []

comm = set(a) & set(b)

if not comm:
  print(0)
  exit()

while comm:
  maxValue = max(comm)
  result.append(maxValue)
  idx1 = a.index(maxValue)
  idx2 = b.index(maxValue)
  a = a[idx1 + 1:]
  b = b[idx2 + 1:]
  comm = set(a) & set(b)

print(len(result))
print(*result)