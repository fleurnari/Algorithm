import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
cardSet = set(card)
maxValue = max(card)
answer = [0 for _ in range(maxValue + 1)]

for i in card:
  if i == maxValue:
    continue
  for j in range(2 * i, maxValue + 1, i):
    if j in cardSet:
      answer[i] += 1
      answer[j] -= 1
for i in card:
  print(answer[i], end = ' ')