import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
pwList = {}

for i in range(n):
  site, pw = map(str, input().split())
  pwList[site] = pw

for i in range(m):
  site = input().rstrip()
  print(pwList[site] + '\n')