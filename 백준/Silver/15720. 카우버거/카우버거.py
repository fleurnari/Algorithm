import sys
input = sys.stdin.readline
b, c, d = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

print(sum(burger) + sum(side) + sum(drink))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)
setCnt = min(b, c, d)
answer = 0

for i in range(setCnt):
  answer += int((burger[i] + side[i] + drink[i]) * 0.9)

answer += sum(burger[setCnt:]) + sum(side[setCnt:]) + sum(drink[setCnt:])

print(answer)