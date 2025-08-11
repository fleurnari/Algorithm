import sys
input = sys.stdin.readline
n = int(input())
wordList = []

for i in range(n):
  wordList.append(input().rstrip())

wordList = list(set(wordList))
wordList.sort(key = lambda x : (len(x), x))
for i in range(len(wordList)):
  print(wordList[i])