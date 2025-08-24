import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pocketmonList = {}

for i in range(1, n + 1):
  pocketmon = input().rstrip()
  pocketmonList[i] = pocketmon
  pocketmonList[pocketmon] = i

for i in range(m):
  command = input().rstrip()
  if command.isdigit():
    print(pocketmonList[int(command)])
  else:
    print(pocketmonList[command])