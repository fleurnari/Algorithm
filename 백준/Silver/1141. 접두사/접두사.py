import sys
input = sys.stdin.readline
n = int(input())
words = [input().strip() for _ in range(n)]
words.sort()
answer = 0

for i in range(n):
  if i == n - 1:
    answer += 1
  elif not words[i + 1].startswith(words[i]):
    answer += 1

print(answer)