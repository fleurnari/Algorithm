import sys

input = sys.stdin.readline

n, m = map(int, input().split())

orgArr = list(map(int, input().split()))

sumArr = [0] * n

cntArr = [0] * m

sumArr[0] = orgArr[0]

answer = 0


for i in range(1, n):
  sumArr[i] = sumArr[i - 1] + orgArr[i]

for i in range(n):
  remainder = sumArr[i] % m
  if (remainder == 0):
    answer += 1
  cntArr[remainder] += 1

for i in range(m):
  if (cntArr[i] > 1):
    answer += (cntArr[i] * (cntArr[i] - 1) // 2)

print(answer)