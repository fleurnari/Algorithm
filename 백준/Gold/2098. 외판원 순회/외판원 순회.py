import sys
input = sys.stdin.readline
n = int(input())
w = []
dpTable = [[0 for j in range(1 << 16)] for i in range(16)]

for i in range(n):
  w.append([])
  w[i] = list(map(int, input().split()))

def tsp(s, e):
  if e == (1 << n) - 1:
    if w[s][0] == 0:
      return float('inf')
    else:
      return w[s][0]
  if dpTable[s][e] != 0:
    return dpTable[s][e]
  minValue = float('inf')
  for i in range(n):
    if (e & (1 << i)) == 0 and w[s][i] != 0:
      minValue = min(minValue, tsp(i, (e | (1 << i))) + w[s][i])
  dpTable[s][e] = minValue
  return dpTable[s][e]

print(tsp(0, 1))