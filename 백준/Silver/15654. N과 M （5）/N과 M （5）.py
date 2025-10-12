import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []

def dfs(x):
  if len(s) == m:
    print(*s)
    return
    
  for i in range(n):
    if arr[i] not in s:
        s.append(arr[i])
        dfs(i + 1)
        s.pop()

dfs(0)