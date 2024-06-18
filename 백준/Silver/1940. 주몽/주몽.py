import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

matList = list(map(int, input().split()))

matList.sort()

i = 0

j = n - 1

answer = 0


while i < j:
  if matList[i] + matList[j] < m:
    i += 1
  elif matList[i] + matList[j] > m:
    j -= 1
  else:
    answer += 1
    i += 1
    j -= 1

print(answer)