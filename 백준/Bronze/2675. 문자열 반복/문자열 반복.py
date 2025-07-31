import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
  r, s = map(str, input().split())
  for j in range(len(s)):
    print(s[j] * int(r), end = '')
  print()