import sys
input = sys.stdin.readline
n = int(input())

cnt = 0
answer = 666
while True:
  if "666" in str(answer):
    cnt += 1

  if cnt == n:
    break

  answer += 1

print(answer)