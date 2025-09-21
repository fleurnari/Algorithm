import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
fruitCategory = {}
left = 0
cnt = 0

for i in range(n):
  current = s[i]
  if current in fruitCategory:
    fruitCategory[current] += 1
  else:
    fruitCategory[current] = 1

  while len(fruitCategory) > 2:
    remove = s[left]
    fruitCategory[remove] -= 1
    if fruitCategory[remove] == 0:
      del fruitCategory[remove]
    left += 1
  cnt = max(cnt, i - left + 1)

print(cnt)