import sys
input = sys.stdin.readline
c, n = map(int, input().split())
costList = [list(map(int, input().split())) for _ in range(n)]
dpTable = [sys.maxsize for _ in range(c + 100)]
dpTable[0] = 0

for cost, customer in costList:
  for i in range(customer, c + 100):
    dpTable[i] = min(dpTable[i], dpTable[i - customer] + cost)

print(min(dpTable[c:]))