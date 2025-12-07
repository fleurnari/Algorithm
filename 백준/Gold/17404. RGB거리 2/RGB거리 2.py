import sys
input = sys.stdin.readline
n = int(input())
rgb = []
answer = sys.maxsize

for _ in range(n):
  rgb.append((list(map(int, input().split()))))

for i in range(3):
  dpTable = [[sys.maxsize] * 3 for _ in range(n)]
  dpTable[0][i] = rgb[0][i]
  for j in range(1, n):
    dpTable[j][0] = min(dpTable[j - 1][1], dpTable[j - 1][2]) + rgb[j][0]
    dpTable[j][1] = min(dpTable[j - 1][0], dpTable[j - 1][2]) + rgb[j][1]
    dpTable[j][2] = min(dpTable[j - 1][0], dpTable[j - 1][1]) + rgb[j][2]

  for j in range(3):
    if i != j:
      answer = min(answer, dpTable[n - 1][j])

print(answer)