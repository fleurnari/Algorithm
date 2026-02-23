import sys
input = sys.stdin.readline
n = int(input())
h = list(map(int, input().split()))
arrow = {}
answer = 0

for height in h:
  if arrow.get(height, 0) > 0:
    arrow[height] -= 1
  else:
    answer += 1

  arrow[height - 1] = arrow.get(height - 1, 0) + 1

print(answer)