import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

k = int(input())

bpt = True

def dfs(v):
    global bpt
    visit[v] = True
    for i in arr[v]:
      if not visit[i]:
        chk[i] = (chk[v] + 1) % 2
        dfs(i)
      elif chk[v] == chk[i]:
        bpt = False


for i in range(k):
  v, e = map(int, input().split())
  arr = [[] for i in range(v + 1)]
  visit = [False] * (v + 1)
  chk = [0] * (v + 1)
  bpt = True

  for i in range(e):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

  for i in range(1, v + 1):
    if bpt:
      dfs(i)
    else:
      break

  if bpt:
    print("YES")
  else:
    print("NO")