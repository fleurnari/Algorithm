import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []


def dfs():
  chk = 0
  
  if len(s) == m:
    tmp = s[0]
    for i in range(1, m):
      if tmp > s[i]:
        return
      else:
        tmp = s[i]
    print(*s)
    return

  for i in range(n):
    if chk != arr[i]:
      s.append(arr[i])
      chk = arr[i]
      dfs()
      s.pop()

dfs()