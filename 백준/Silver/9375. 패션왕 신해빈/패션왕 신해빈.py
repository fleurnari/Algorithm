import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
  clothes = {}
  n = int(input())
  for j in range(n):
    name, category = map(str, input().split())
    if category in clothes:
      clothes[category].append(name)
    else:
      clothes[category] = [name]

  result = 1

  for k in clothes:
    result *= (len(clothes[k]) + 1)

  print(result - 1)