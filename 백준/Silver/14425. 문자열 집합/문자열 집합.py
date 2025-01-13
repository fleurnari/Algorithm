import sys
input = sys.stdin.readline
n, m = map(int, input().split())
wordList = set([input() for i in range(n)])
result = 0

for i in range(m):
  tmpWord = input()
  if tmpWord in wordList:
    result += 1

print(result)