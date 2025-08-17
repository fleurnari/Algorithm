import sys
input = sys.stdin.readline
n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))
answer = {}

for i in nArr:
  if i in answer:
    answer[i] += 1
  else:
    answer[i] = 1

for i in mArr:
  result = answer.get(i)
  if result == None:
    print(0, end = ' ')
  else:
    print(result, end = ' ')