import sys
input = sys.stdin.readline
k = int(input())
sign = list(input().split())
visited = [False] * 10
minVal = ""
maxVal = ""

def check(a, b, s):
  if s == '<':
    return a < b
  else:
    return a > b

def dfs(depth, num):
  global minVal, maxVal
  
  if depth == k + 1:
    if not minVal:
      minVal = num
    else:
      maxVal = num
    return

  for i in range(10):
    if not visited[i]:
      if depth == 0 or check(int(num[-1]), i, sign[depth - 1]):
        visited[i] = True
        dfs(depth + 1, num + str(i))
        visited[i] = False


dfs(0, "")
print(maxVal)
print(minVal)