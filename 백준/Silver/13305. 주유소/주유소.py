import sys
input = sys.stdin.readline
n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
minPrice = price[0]
sum = 0

for i in range(n - 1):
  if price[i] < minPrice:
    minPrice = price[i]
  sum += minPrice * dist[i]

print(sum)