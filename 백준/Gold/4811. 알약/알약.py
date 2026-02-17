import sys
input = sys.stdin.readline
dp = [[0] * 31 for _ in range(31)]

for h in range(31):
  dp[0][h] = 1

for w in range(1, 31):
  for h in range(31):
    if h > 0:
      dp[w][h] += dp[w][h - 1]
    
    if h < 30:
      dp[w][h] += dp[w - 1][h + 1]

while True:
  n = int(input())
  if n == 0:
    break
  print(dp[n][0])