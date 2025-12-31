import sys
input = sys.stdin.readline
n = int(input())
w = []
dpTable = [[0 for j in range(1 << 16)] for i in range(16)]

for i in range(n):
  w.append([])
  w[i] = list(map(int, input().split()))

def tsp(c, v):
  if v == (1 << n) - 1:
    if w[c][0] == 0:
      return float('inf')
    else:
      return w[c][0]
  if dpTable[c][v] != 0:
    return dpTable[c][v]
  minValue = float('inf')
  for i in range(n):
    if (v & (1 << i)) == 0 and w[c][i] != 0:
      minValue = min(minValue, tsp(i, (v | (1 << i))) + w[c][i])
  dpTable[c][v] = minValue
  return dpTable[c][v]

print(tsp(0, 1))