import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
visitList = [False] * n

def dfs():
  chk = 0
  if len(s) == m:
    print(*s)
    return

  for i in range(n):
    if chk != arr[i] and not visitList[i]:
      s.append(arr[i])
      visitList[i] = True
      chk = arr[i]
      dfs()
      s.pop()
      visitList[i] = False

dfs()