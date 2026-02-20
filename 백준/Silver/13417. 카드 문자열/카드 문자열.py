import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  seq = input().split()
  result = seq[0]
  
  for i in range(1, n):
    if seq[i] <= result[0]:
      result = seq[i] + result
    else:
      result = result + seq[i]

  print(result)