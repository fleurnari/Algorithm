import sys
input = sys.stdin.readline
n = int(input())
sum = 1
answer = 0

for i in range(1, n + 1):
  sum *= i

sum = list(str(sum))

for i in range(len(sum) - 1, -1, -1):
  if sum[i] != '0':
    break
  answer += 1

print(answer)