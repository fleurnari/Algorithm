import sys
input = sys.stdin.readline
n = int(input())
visitList = [0] * n
answer = 0

def chk(current):
  for i in range(current):
    if visitList[current] == visitList[i] or current - i == abs(visitList[current] - visitList[i]):
      return False
  return True

def dfs(x):
  global answer

  if x == n:
    answer += 1
  else:
    for i in range(n):
      visitList[x] = i
      if chk(x):
        dfs(x + 1)

dfs(0)
print(answer)