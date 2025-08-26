import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coinArr = []
coin = 0

for i in range(n):
  coinArr.append(int(input()))

coinArr.sort(reverse=True)

for i in range(len(coinArr)):
  coin += k // coinArr[i]
  k %= coinArr[i]

print(coin)